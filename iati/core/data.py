"""A module containing a core representation of an IATI Dataset."""
from lxml import etree
import iati.core.exceptions
import iati.core.utilities


class Dataset(object):
    """Representation of an IATI XML file that may be validated against a schema.

    Attributes:
        strictly_valid (bool): Whether the dataset must strictly conform to the IATI standard.
            If strictly conforming, invalid elements and attributes will be removed.
        xml_str (str): A string representation of the XML being represented.
        xml_tree (ElementTree): A tree representation of the XML being represented.

    Note:
        The current content of the dataset is deemed to be that which was last asigned to either self.xml_str or self.xml_tree.

    Warning:
        The behaviour of simultaneous assignment to both self.xml_str and self.xml_tree is undefined.

    Todo:
        Implement getters and setters for attributes.
        Implement an addition override to allow for combation of datasets.
    """

    def __init__(self, xml, strictly_valid=False):
        """Initialise a dataset.

        Args:
            xml (str/ElementTree): A representation of the XML to encapsulate.
                May be either a string or an ElementTree.
            strictly_valid (bool, optional): Whether the dataset must strictly conform to the IATI standard.
                Defaults to False.

        Raises:
            TypeError: If an attempt to pass something that is not a string or ElementTree is made.
            ValueError: If a provided XML string is not valid XML.
            iati.core.exceptions.ValidationError:
                If the provided XML should conform to the IATI standard, but does not.

        Todo:
            Undertake validation.
        """
        if isinstance(xml, etree._Element):
            self.xml_tree = xml
        else:
            self.xml_str = xml

    @property
    def xml_str(self):
        return self._xml_str

    @xml_str.setter
    def xml_str(self, value):
        self.xml_tree = value
        self._xml_str = value

    @property
    def xml_tree(self):
        return self._xml_tree

    @xml_tree.setter
    def xml_tree(self, value):
        if isinstance(value, etree._Element):
            self._xml_tree = value
            self._xml_str = etree.tostring(value, pretty_print=True)
        else:
            try:
                self._xml_tree = etree.fromstring(value)
                self._xml_str = value
            except etree.XMLSyntaxError:
                msg = "The string provided to create a Dataset from is not valid XML."
                iati.core.utilities.log_error(msg)
                raise ValueError(msg)
            except ValueError:
                msg = "Datasets can only be created from ElementTrees or strings containing valid XML. Actual type: {0}".format(type(value))
                iati.core.utilities.log_error(msg)
                raise TypeError(msg)
