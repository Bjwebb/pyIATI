"""A module containing validation functionality."""

from lxml import etree
import iati.core.default


class ValidationError(object):
    """A base class to encapsulate information about Validation Errors."""

    def __init__(self, err_name, calling_locals=dict()):
        """Create a new ValidationError.

        Args:
            err_name (str): The name of the error to use as a base.
            calling_locals (dict): The dictionary of local variables from the calling scope. Obtained by calling `locals()`. Default is an empty dictionary.

        Raises:
            ValueError: If there is no base error with the provided name.

        Todo:
            Split message formatting into a child class and raise an error when variables are missing.

        """
        try:
            err_detail = _ERROR_CODES[err_name]
        except (KeyError, TypeError):
            raise ValueError('{err_name} is not a known type of ValidationError.'.format(**locals()))

        # set general attributes for this type of error
        for key, val in err_detail.items():
            setattr(self, key, val)

        self.status = 'error' if err_name.split('-')[0] =='err' else 'warning'

        # format error messages with context-specific info
        try:
            self.help = self.help.format(**calling_locals)
            self.info = self.info.format(**calling_locals)
        except KeyError as missing_var_err:
            # raise NameError('The calling scope must contain a `{missing_var_err.args[0]}` variable for providing information for the error message.'.format(**locals()))
            pass

        # set general attributes for this type of error that require context from the calling scope
        try:
            self.line_number = calling_locals['line_number']
            self.context = calling_locals['dataset'].source_around_line(self.line_number)
        except KeyError:
            # TODO: Determine what the defaults should be should the appropriate values not be available
            pass


class ValidationErrorLog(list):
    """A container to keep track of a set of ValidationErrors."""

    def contains_errors(self):
        """Determine whether there are errors contained.

        Note:
            The error log may contain warnings, or may be empty.

        Returns:
            bool: Whether there are errors within this error log.

        """
        actual_errors = [err for err in self if err.status == 'error']

        return len(actual_errors) > 0


_ERROR_CODES = {
    'err-code-not-on-codelist': {
        'category': 'codelist',
        'description': 'An attribute that requires a Code from a particular complete Codelist contained a value not on the Codelist.',
        'info': '{code} is not a valid Code on the {codelist.name} Codelist.',
        'help': 'The `{attr_name}` attribute must contain a value on the `{codelist.name}` Codelist.\nSee http://iatistandard.org/202/codelists/{codelist.name} for permitted values.'
    },
    'warn-code-not-on-codelist': {
        'category': 'codelist',
        'description': 'An attribute that should contain a Code from a particular incomplete Codelist contained a value not on the Codelist.',
        'info': '{code} is not a Code on the {codelist.name} Codelist. ',
        'help': 'The `{attr_name}` attribute should contain a value on the `{codelist.name}` Codelist. Note that values not on the Codelist may be valid in particular circumstances.\nSee http://iatistandard.org/202/codelists/{codelist.name} for values on the Codelist.'
    }
}


def _check_codes(dataset, codelist):
    """Determine whether a given Dataset has values from the specified Codelist where expected.

    Args:
        dataset (iati.core.data.Dataset): The Dataset to check Codelist values within.
        codelist (iati.core.codelists.Codelist): The Codelist to check values from.

    Returns:
        iati.validator.ValidationErrorLog: A log of the errors that occurred.

    """
    error_log = ValidationErrorLog()
    mappings = iati.core.default.codelist_mapping()

    for mapping in mappings[codelist.name]:
        base_xpath = mapping['xpath']
        condition = mapping['condition']
        split_xpath = base_xpath.split('/')
        parent_el_xpath = '/'.join(split_xpath[:-1])
        attr_name = split_xpath[-1:][0][1:]

        if condition is None:
            parent_el_xpath = parent_el_xpath + '[@' + attr_name + ']'
        else:
            parent_el_xpath = parent_el_xpath + '[' + condition + ' and @' + attr_name + ']'

        parents_to_check = dataset.xml_tree.xpath(parent_el_xpath)

        for parent in parents_to_check:
            code = parent.attrib[attr_name]

            if code not in codelist.codes:
                line_number = parent.sourceline

                if codelist.complete:
                    error = ValidationError('err-code-not-on-codelist', locals())
                else:
                    error = ValidationError('warn-code-not-on-codelist', locals())

                error.actual_value = code

                error_log.append(error)

    return error_log


def _check_codelist_values(dataset, schema):
    """Check whether a given Dataset has values from Codelists that have been added to a Schema where expected.

    Args:
        dataset (iati.core.data.Dataset): The Dataset to check Codelist values within.
        schema (iati.core.schemas.Schema): The Schema to locate Codelists within.

    Returns:
        iati.validator.ValidationErrorLog: A log of the errors that occurred.

    """
    error_log = ValidationErrorLog()

    for codelist in schema.codelists:
        error_log.extend(_check_codes(dataset, codelist))

    return error_log


def _correct_codelist_values(dataset, schema):
    """Determine whether a given Dataset has values from Codelists that have been added to a Schema where expected.

    Args:
        dataset (iati.core.data.Dataset): The Dataset to check Codelist values within.
        schema (iati.core.schemas.Schema): The Schema to locate Codelists within.

    Returns:
        bool: If `error_log` is False. A boolean indicating whether the given Dataset has values from the specified Codelists where they should be.

    """
    error_log = _check_codelist_values(dataset, schema)

    return not error_log.contains_errors()


def full_validation(dataset, schema):
    """Perform full validation on a Dataset.

    Args:
        dataset (iati.core.Dataset): The Dataset to check validity of.
        schema (iati.core.Schema): The Schema to validate the Dataset against.

    Warning:
        Parameters are likely to change in some manner.

    Returns:
        list of dict: A list of dictionaries containing error output. An empty list indicates that there are no errors.

    Todo:
        Create test against a bad Schema.

    """
    return _check_codelist_values(dataset, schema)


def is_iati_xml(dataset, schema):
    """Determine whether a given Dataset's XML is valid against the specified Schema.

    Args:
        dataset (iati.core.data.Dataset): The Dataset to check validity of.
        schema (iati.core.schemas.Schema): The Schema to validate the Dataset against.

    Warning:
        Parameters are likely to change in some manner.

    Returns:
        bool: A boolean indicating whether the given Dataset is valid XML against the given Schema.

    Raises:
        iati.core.exceptions.SchemaError: An error occurred in the parsing of the Schema.

    Todo:
        Create test against a bad Schema.

    """
    try:
        validator = schema.validator()
    except iati.core.exceptions.SchemaError as err:
        raise err

    try:
        validator.assertValid(dataset.xml_tree)
    except etree.DocumentInvalid:
        return False

    return True


def is_valid(dataset, schema):
    """Determine whether a given Dataset is valid against the specified Schema.

    Args:
        dataset (iati.core.Dataset): The Dataset to check validity of.
        schema (iati.core.Schema): The Schema to validate the Dataset against.

    Warning:
        Parameters are likely to change in some manner.

    Returns:
        bool: A boolean indicating whether the given Dataset is valid against the given Schema.

    Todo:
        Create test against a bad Schema.

    """
    try:
        iati_xml = is_iati_xml(dataset, schema)
        if not iati_xml:
            return False
    except iati.core.exceptions.SchemaError:
        return False

    return _correct_codelist_values(dataset, schema)


def is_xml(maybe_xml):
    """Determine whether a given parameter is XML.


    Args:
        maybe_xml (str): An string that may or may not contain valid XML.

    Returns:
        bool: A boolean indicating whether the given Dataset is valid XML.

    """
    if isinstance(maybe_xml, iati.core.data.Dataset):
        maybe_xml = maybe_xml.xml_str

    try:
        _ = etree.fromstring(maybe_xml.strip())
        return True
    except (etree.XMLSyntaxError, AttributeError, TypeError, ValueError):
        return False

