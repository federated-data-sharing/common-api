import connexion
import six

from swagger_server.models.dcat_metadata import DCATMetadata  # noqa: E501
from swagger_server.models.data_dictionary import DataDictionary  # noqa: E501
from swagger_server.models.datasets_list import DatasetsList  # noqa: E501
from swagger_server import util


def datasets_datasetid_catalogue_get(datasetid):  # noqa: E501
    """Get Catalogue Entry (Metadata) for Dataset

    Returns a DCAT dataset catalogue entry # noqa: E501

    :param datasetid: Dataset ID
    :type datasetid: str

    :rtype: DCATMetadata
    """
    return 'do some magic!'


def datasets_datasetid_dictionary_get(datasetid):  # noqa: E501
    """Get a Dataset Definition

    Obtain a dataset definition (adhering to the schema.org vocabulary) # noqa: E501

    :param datasetid: Dataset ID
    :type datasetid: str

    :rtype: DataDictionary
    """
    return 'do some magic!'


def datasets_get(doi=None, title=None, author=None, description=None, organisation=None, tag_key=None, tag_value=None):  # noqa: E501
    """Get a List of Datasets that can be Filtered

    Returns a list of datasets within the Dataset Registry # noqa: E501

    :param doi: The DOI of the dataset
    :type doi: str
    :param title: The title of the dataset
    :type title: str
    :param author: The specified author of the dataset
    :type author: str
    :param description: The description of the dataset
    :type description: str
    :param organisation: The description of the dataset
    :type organisation: str
    :param tag_key: The tag key applied to the dataset
    :type tag_key: str
    :param tag_value: The tag key applied to the dataset
    :type tag_value: str

    :rtype: DatasetsList
    """
    return 'do some magic!'
