"""A module containing utility constants and functions for tests.

A large number of constants containing example file content are contained. These constants are named from left to right, with general properties first, then leading into more specific information. These names indicate what they are used for.

Example:
    To load a file into a string::

        name_of_file = 'a-file-name-without-the-extension'
        CONSTANT_NAME = iati.core.resources.load_as_string(iati.core.resources.get_test_data_path(name_of_file))

Note:
    The current method of managing test data is known to be sub-optimal. Suggestions for better methods that satisfy requirements are appreciated!

Todo:
    Add versions of constants that are valid for differing schema versions.

"""
import decimal
from lxml import etree
import iati.core.resources


DATASET_FOR_ATLEASTONE_RULE_VALID = iati.core.resources.load_as_dataset(iati.core.resources.get_test_data_path('valid_atleastone'))
"""An etree containing XML data that is permitted by `RuleAtLeastOne`."""
DATASET_FOR_ATLEASTONE_RULE_INVALID = iati.core.resources.load_as_dataset(iati.core.resources.get_test_data_path('invalid_atleastone'))
"""An etree containing XML data that is not permitted by `RuleAtLeastOne`."""

DATASET_FOR_DATEORDER_RULE_VALID = iati.core.resources.load_as_dataset(iati.core.resources.get_test_data_path('valid_dateorder'))
"""An etree containing XML data that is permitted by `RuleDateOrder`."""
DATASET_FOR_DATEORDER_RULE_INVALID = iati.core.resources.load_as_dataset(iati.core.resources.get_test_data_path('invalid_dateorder'))
"""An etree containing XML data that is not permitted by `RuleDateOrder`."""
DATASET_FOR_DATEORDER_RULE_INVALID_DATE_FORMAT = iati.core.resources.load_as_dataset(iati.core.resources.get_test_data_path('invalid_format_dateorder'))
"""An etree containing XML data that contains dates that are formatted incorrectly according to RuleDateOrder."""

DATASET_FOR_DEPENDENT_RULE_VALID = iati.core.resources.load_as_dataset(iati.core.resources.get_test_data_path('valid_dependent'))
"""An etree containing XML data that is permitted by `RuleDependent`."""
DATASET_FOR_DEPENDENT_RULE_INVALID = iati.core.resources.load_as_dataset(iati.core.resources.get_test_data_path('invalid_dependent'))
"""An etree containing XML data that is not permitted by `RuleDependent`."""

DATASET_FOR_NOMORETHANONE_RULE_VALID = iati.core.resources.load_as_dataset(iati.core.resources.get_test_data_path('valid_nomorethanone'))
"""An etree containing XML data that is permitted by `RuleNoMoreThanOne`."""
DATASET_FOR_NOMORETHANONE_RULE_INVALID = iati.core.resources.load_as_dataset(iati.core.resources.get_test_data_path('invalid_nomorethanone'))
"""An etree containing XML data that is not permitted by `RuleNoMoreThanOne`."""

DATASET_FOR_REGEXMATCHES_RULE_VALID = iati.core.resources.load_as_dataset(iati.core.resources.get_test_data_path('valid_regexmatches'))
"""An etree containing XML data that is permitted by `RuleRegexMatches`."""
DATASET_FOR_REGEXMATCHES_RULE_INVALID = iati.core.resources.load_as_dataset(iati.core.resources.get_test_data_path('invalid_regexmatches'))
"""An etree containing XML data that is not permitted by `RuleRegexMatches`."""

DATASET_FOR_REGEXNOMATCHES_RULE_VALID = iati.core.resources.load_as_dataset(iati.core.resources.get_test_data_path('valid_regexnomatches'))
"""An etree containing XML data that is permitted by `RuleRegexNoMatches`."""
DATASET_FOR_REGEXNOMATCHES_RULE_INVALID = iati.core.resources.load_as_dataset(iati.core.resources.get_test_data_path('invalid_regexnomatches'))
"""An etree containing XML data that is not permitted by `RuleRegexNoMatches`."""

DATASET_FOR_STARTSWITH_RULE_VALID = iati.core.resources.load_as_dataset(iati.core.resources.get_test_data_path('valid_startswith'))
"""An etree containing XML data that is permitted by `RuleStartsWith`."""
DATASET_FOR_STARTSWITH_RULE_INVALID = iati.core.resources.load_as_dataset(iati.core.resources.get_test_data_path('invalid_startswith'))
"""An etree containing XML data that is not permitted by `RuleStartsWith`."""

DATASET_FOR_SUM_RULE_VALID = iati.core.resources.load_as_dataset(iati.core.resources.get_test_data_path('valid_sum'))
"""An etree containing XML data that is permitted by `RuleSum`."""
DATASET_FOR_SUM_RULE_INVALID = iati.core.resources.load_as_dataset(iati.core.resources.get_test_data_path('invalid_sum'))
"""An etree containing XML data that is not permitted by `RuleSum`."""

DATASET_FOR_UNIQUE_RULE_VALID = iati.core.resources.load_as_dataset(iati.core.resources.get_test_data_path('valid_unique'))
"""An etree containing XML data that is permitted by `RuleUnique`."""
DATASET_FOR_UNIQUE_RULE_INVALID = iati.core.resources.load_as_dataset(iati.core.resources.get_test_data_path('invalid_unique'))
"""An etree containing XML data that is not permitted by `RuleUnique`."""

SCHEMA_NAME_VALID = 'iati-activities-schema'
"""A string containing a valid Schema name."""

XML_STR_VALID_NOT_IATI = '<parent><child attribute="value" /></parent>'
"""A string containing valid XML that is not valid against the IATI schema."""
XML_STR_VALID_IATI = iati.core.resources.load_as_string(iati.core.resources.get_test_data_path('valid'))
"""A string containing valid IATI XML."""
XML_STR_VALID_IATI_INVALID_CODE = iati.core.resources.load_as_string(iati.core.resources.get_test_data_path('valid_iati_invalid_code'))
"""A string containing valid IATI XML, but an invalid Code valid."""
XML_STR_INVALID = iati.core.resources.load_as_string(iati.core.resources.get_test_data_path('invalid'))
"""A string that is not valid XML."""
XML_STR_LEADING_WHITESPACE = iati.core.resources.load_as_string(iati.core.resources.get_test_data_path('leading_whitespace_xml'))
"""A string containing valid XML apart form leading whitepace before an `<?xml` declaration."""

XML_STR_INVALID_IATI_MISSING_REQUIRED_ELEMENT = iati.core.resources.load_as_string(iati.core.resources.get_test_data_path('invalid_iati_missing_required_element'))
"""A string containing invalid IATI XML. It is invalid due to a missing element defined as require in iati-common.xsd"""
XML_STR_INVALID_IATI_MISSING_REQUIRED_ELEMENT_COMMON = iati.core.resources.load_as_string(iati.core.resources.get_test_data_path('invalid_iati_missing_required_element_from_common'))
"""A string containing invalid IATI XML. It is invalid due to a missing element defined as require in iati-common.xsd"""

XML_STR_VALID_IATI_VALID_CODE_FROM_COMMON = iati.core.resources.load_as_string(iati.core.resources.get_test_data_path('valid_iati_valid_code_from_common'))
"""A string containing valid IATI XML containing an element that is defined in iati-common.xsd - it has an attribute with a value on the appropriate Codelist."""
XML_STR_VALID_IATI_INVALID_CODE_FROM_COMMON = iati.core.resources.load_as_string(iati.core.resources.get_test_data_path('valid_iati_invalid_code_from_common'))
"""A string containing valid IATI XML containing an element that is defined in iati-common.xsd - it has an attribute with a value that is not on the appropriate Codelist."""

XML_STR_VALID_IATI_VALID_CODES_MULTIPLE_XPATHS_FOR_CODELIST = iati.core.resources.load_as_string(iati.core.resources.get_test_data_path('valid_iati_valid_codes_multiple_xpaths_for_codelist'))
"""A string contains valid IATI XML containing attributes on multiple elements that require values from the same Codelist. Each of the values from the Codelist are correct."""
XML_STR_VALID_IATI_INVALID_CODES_MULTIPLE_XPATHS_FOR_CODELIST_FIRST = iati.core.resources.load_as_string(iati.core.resources.get_test_data_path('valid_iati_invalid_codes_multiple_xpaths_for_codelist_first'))
"""A string contains valid IATI XML containing attributes on multiple elements that require values from the same Codelist.

The first value that should be from the Codelist is valid, while the second is invalid."""
XML_STR_VALID_IATI_INVALID_CODES_MULTIPLE_XPATHS_FOR_CODELIST_SECOND = iati.core.resources.load_as_string(iati.core.resources.get_test_data_path('valid_iati_invalid_codes_multiple_xpaths_for_codelist_second'))
"""A string contains valid IATI XML containing attributes on multiple elements that require values from the same Codelist.

The first value that should be from the Codelist is invalid, while the second is valid."""

XML_STR_VALID_IATI_VOCAB_DEFAULT_EXPLICIT = iati.core.resources.load_as_string(iati.core.resources.get_test_data_path('valid_iati_vocab_default_explicit'))
"""A string containing valid IATI XML containing an element that uses vocabularies. Explicitly defines default vocab and uses code from that list."""
XML_STR_VALID_IATI_VOCAB_DEFAULT_IMPLICIT = iati.core.resources.load_as_string(iati.core.resources.get_test_data_path('valid_iati_vocab_default_implicit'))
"""A string containing valid IATI XML containing an element that uses vocabularies. Implicitly assumes default vocab and uses code from that list."""
XML_STR_VALID_IATI_VOCAB_DEFAULT_IMPLICIT_INVALID_CODE = iati.core.resources.load_as_string(iati.core.resources.get_test_data_path('valid_iati_vocab_default_implicit_invalid_code'))
"""A string containing valid IATI XML containing an element that uses vocabularies. Implicitly assumes default vocab and uses code not in list."""
XML_STR_VALID_IATI_VOCAB_NON_DEFAULT = iati.core.resources.load_as_string(iati.core.resources.get_test_data_path('valid_iati_vocab_non_default'))
"""A string contains valid IATI XML containing an element that uses vocabularies. Explicitly defines non-default vocab and uses code from that list."""
XML_STR_VALID_IATI_VOCAB_MULTIPLE_SAME_VALID = iati.core.resources.load_as_string(iati.core.resources.get_test_data_path('valid_iati_vocab_multiple_same_valid'))
"""A string contains valid IATI XML containing an activity that uses multiple instances of the same element that uses vocabularies. The vocabulary used by each of these elements is the same. @code values are valid. Percentages add up to 100."""
XML_STR_VALID_IATI_VOCAB_MULTIPLE_DIFFERENT_VALID = iati.core.resources.load_as_string(iati.core.resources.get_test_data_path('valid_iati_vocab_multiple_different_valid'))
"""A string contains valid IATI XML containing an activity that uses multiple instances of the same element that uses vocabularies. The vocabulary used by each of these elements is different. @code values are valid.Percentages add up to 100."""
XML_STR_VALID_IATI_VOCAB_MULTIPLE_SAME_INVALID_CODE = iati.core.resources.load_as_string(iati.core.resources.get_test_data_path('valid_iati_vocab_multiple_same_invalid_code'))
"""A string contains valid IATI XML containing an activity that uses multiple instances of the same element that uses vocabularies. The vocabulary used by each of these elements is the same. @code values are not valid. Percentages add up to 100."""
XML_STR_VALID_IATI_VOCAB_MULTIPLE_DIFFERENT_INVALID_CODE = iati.core.resources.load_as_string(iati.core.resources.get_test_data_path('valid_iati_vocab_multiple_different_invalid_code'))
"""A string contains valid IATI XML containing an activity that uses multiple instances of the same element that uses vocabularies. The vocabulary used by each of these elements is different. @code values are not valid. Percentages add up to 100."""

XML_STR_VALID_IATI_VOCAB_USER_DEFINED = iati.core.resources.load_as_string(iati.core.resources.get_test_data_path('valid_iati_vocab_user_defined'))
"""A string containing valid IATI XML containing an element that uses vocabularies. Specifies user-defined vocabulary. No URI specified."""
XML_STR_VALID_IATI_VOCAB_USER_DEFINED_WITH_URI_READABLE = iati.core.resources.load_as_string(iati.core.resources.get_test_data_path('valid_iati_vocab_user_defined_with_uri_readable'))
"""A string containing valid IATI XML containing an element that uses vocabularies. Specifies user-defined vocabulary. URI specified and machine readable. Uses code from this list."""
XML_STR_VALID_IATI_VOCAB_USER_DEFINED_WITH_URI_READABLE_BAD_CODE = iati.core.resources.load_as_string(iati.core.resources.get_test_data_path('valid_iati_vocab_user_defined_with_uri_readable_bad_code'))
"""A string containing valid IATI XML containing an element that uses vocabularies. Specifies user-defined vocabulary. URI specified and machine readable. Uses code not in list."""
XML_STR_VALID_IATI_VOCAB_USER_DEFINED_WITH_URI_UNREADABLE = iati.core.resources.load_as_string(iati.core.resources.get_test_data_path('valid_iati_vocab_user_defined_with_uri_unreadable'))
"""A string containing valid IATI XML containing an element that uses vocabularies. Specifies user-defined vocabulary. URI specified and not machine readable."""

XML_TREE_VALID = etree.fromstring(XML_STR_VALID_NOT_IATI)
"""An etree that is not valid IATI data."""
XML_TREE_VALID_IATI = etree.fromstring(XML_STR_VALID_IATI)
"""A valid IATI etree."""
XML_TREE_VALID_IATI_INVALID_CODE = etree.fromstring(XML_STR_VALID_IATI_INVALID_CODE)
"""A valid IATI etree that has an invalid Code value."""

TYPE_TEST_DATA = {
    'bool': [True, False],
    'bytes': [],  # counts as a string, so moved there
    'bytearray': [bytearray.fromhex('2Ef0 F1f2  '), bytearray(b'Hi!'), bytearray(range(20))],
    'complex': [3453J, -35415J, 0J, complex(234, 681), complex(-768, 16078), complex(6187, -81), complex(-1867, -618)],
    'contextmanager': [decimal.localcontext()],
    'float': [-2343324.534, 0.0, 32423.34, 1.3e7, float('Infinity'), float('nan'), float('-inf')],
    'function': [dir, hash, map, max, type],
    'int': [-234, 0, 2131908],
    'iter': [iter([1, 2, 3])],
    'list': [[], [1, 23], ['varying', 7, b'ypes', []]],
    'mapping': [{}, dict(zip(['one', 'two', 'three'], [1, 2, 3])), dict(one=1, two=2, three=3)],
    'memory': [memoryview(b'abcefg')],
    'none': [None],
    'other': [NotImplemented],
    'range': [range(3, 4)],
    'set': [set(range(20)), set(['hello', 23]), frozenset(range(20)), frozenset(['hello', 23])],
    'str': [SCHEMA_NAME_VALID, XML_STR_VALID_NOT_IATI, XML_STR_INVALID, b'\x80abc', b'\x80abc', '\N{GREEK CAPITAL LETTER DELTA}', '\u0394', '\U00000394'],
    'tuple': [(), (1, 2)],
    'type': [type(1), type('string')],
    'unicode': [],  # counts as a string, so moved there
    'view': [{}.keys(), dict(zip(['one', 'two', 'three'], [1, 2, 3])).items(), dict(one=1, two=2, three=3).values()]
}
"""Generic test data of various Python builtin types."""


def find_parameter_by_type(types, type_as_specified=True):
    """Find a number of values of the specified type to pass to a test function.

    Args:
        types (list of str): The types of parameter that should be looked for.
        type_as_specified (bool): Whether to look for values as specified or everything else. Default True.

    Returns:
        list: A list of values to pass to the test function.

    """
    valid_keys_as_specified = [key for key in types if key in TYPE_TEST_DATA]
    if not type_as_specified:
        valid_keys = [key for key in TYPE_TEST_DATA.keys() if key not in valid_keys_as_specified]
    else:
        valid_keys = valid_keys_as_specified

    results = []

    for key in valid_keys:
        results = results + TYPE_TEST_DATA[key]

    return results
