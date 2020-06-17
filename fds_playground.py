import requests, json
import os
import yaml
import jsonschema

FDS_ENDPOINT = "https://localhost:8443/aridhia/federated-data-sharing/1.0.0"
# dataset_id = 'synthetic_alzheimers_profile'
dataset_id = 'oasis_longitudinal'

def run_query_datasets_get():
    r = requests.get(f'{FDS_ENDPOINT}/datasets', verify=False)
    print(r)
    dataset_list = r.json()
    # print(json.dumps(dataset_list, sort_keys=True, indent=4))
    return dataset_list
dataset_list = run_query_datasets_get()
print(dataset_list)


def run_query_catalogue():
    r = requests.get(f'{FDS_ENDPOINT}/datasets/{dataset_id}/catalogue', verify=False)
    print(r)
    dataset_cat = r.json()
    # print(json.dumps(dataset_list, sort_keys=True, indent=4))
    return dataset_cat
dataset_cat = run_query_catalogue()
print(dataset_cat)

def run_query_dictionary():
    r = requests.get(f'{FDS_ENDPOINT}/datasets/{dataset_id}/dictionary', verify=False)
    print(r)
    dataset_dict = r.json()
    # print(json.dumps(dataset_list, sort_keys=True, indent=4))
    return dataset_dict
dataset_dict = run_query_dictionary()
print(dataset_dict)


api_file = 'src/reference_api/swagger_server/swagger/swagger.yaml'
with open(api_file, 'r') as file:
    full_schema = yaml.load(file, Loader=yaml.FullLoader)
    
# This gets it to resolve all the $refs in the schema on itself
resolver = jsonschema.RefResolver('', full_schema)

def validate_json(JSON, schema):
    try:
        jsonschema.validate(JSON, schema=schema, resolver=resolver)
        print('Successful Validation!')
    except Exception as e:
        print(e)

schema_datasets_list = full_schema['components']['schemas']["datasets_list"]
schema_DCAT_metadat = full_schema['components']['schemas']["DCAT_metadata"]
schema_data_dictionary = full_schema['components']['schemas']["data_dictionary"]

validate_json(dataset_list, schema_datasets_list)
validate_json(dataset_cat, schema_DCAT_metadat)
validate_json(dataset_dict, schema_data_dictionary)

################################    
################################
################################
################################
# approved_registry_dict = {'approved_registries': [{'registry_id': 'test_string1',
                                # 'registry_name': 'test_string2',
                                # 'registry_host': 'test_string3',
                                # 'registry_url': 'test_string4'}]}

# approved_registry_dict = {'approved_registries': [{"registry_id": 'test_string1',
                                # "registry_name": 2,
                                # "registry_host": {"dummy": "dummy"},
                                # "registry_url": 'test_string4'}]}
                                
# approved_registry_dict = {'approved_registries': 'test string'}


# api_file = 'FDS/swagger_server/swagger/swagger.yaml'
# with open(api_file, 'r') as file:
    # data = yaml.load(file, Loader=yaml.FullLoader)
# print(data)

# print(data['components']['schemas']["approved_registries"])

# This gets it to resolve on itself
# resolver = jsonschema.RefResolver('', data)

# jsonschema.validate(approved_registry_dict, schema=data['components']['schemas']["approved_registries"], resolver=resolver)
################################
################################
################################
################################
