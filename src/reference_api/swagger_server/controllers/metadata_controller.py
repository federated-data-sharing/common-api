import connexion
import six
import json

from swagger_server.aridhia_integration import dummy_returns

from swagger_server.models.dcat_metadata import DCATMetadata  # noqa: E501
from swagger_server.models.data_dictionary_list import DataDictionaryList  # noqa: E501
from swagger_server.models.datasets_list import DatasetsList  # noqa: E501
from swagger_server import util


def datasets_datasetid_catalogue_get(datasetid):  # noqa: E501
    """Get Catalogue Entry (Metadata) for Dataset

    Returns a DCAT dataset catalogue entry # noqa: E501

    :param datasetid: Dataset ID
    :type datasetid: str

    :rtype: DCATMetadata
    """
    
    ## TODO return 404 if dataset cannot be found
    if datasetid == "invalid_id_nopermission":
        return f" 401 - You do not have permission so see the dataset '{datasetid}'", 401
    
    ## TODO return 404 if dataset cannot be found
    if datasetid == "invalid_id_missing":
        return f" 404 - Dataset id '{datasetid}' cannot be found", 404
    
    r = dummy_returns.dataset_catalogue_dummy()
    response = json.loads(r)
    print(response)
    print(type(response))
    print("Creating DCATMetadata...")
    output = DCATMetadata.from_dict(response)
    print(output)
    print("Returning output")
    return output


def datasets_datasetid_dictionary_get(datasetid):  # noqa: E501
    """Get a Dataset Definition

    Obtain a dataset definition (adhering to the schema.org vocabulary) # noqa: E501

    :param datasetid: Dataset ID
    :type datasetid: str

    :rtype: DataDictionaryList
    """
    
    ## TODO return 404 if dataset cannot be found
    if datasetid == "invalid_id_nopermission":
        return f" 401 - You do not have permission so see the dataset '{datasetid}'", 401
    
    ## TODO return 404 if dataset cannot be found
    if datasetid == "invalid_id_missing":
        return f" 404 - Dataset id '{datasetid}' cannot be found", 404
    
    r = dummy_returns.dataset_dictionary_dummy()
    response = json.loads(r)
    print(response)
    print(type(response))
    print("Creating DataDictionaryList...")
    output = DataDictionaryList.from_dict(response)
    print(output)
    print("Returning output")
    return output

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
    
    r = dummy_returns.dataset_list_dummy()
    response = json.loads(r)
    print(response)
    print(type(response))
    print("Creating DatasetsList...")
    output = DatasetsList.from_dict(response)
    print(output)
    print("Returning output")
    return output
