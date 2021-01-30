# Using Python

> Back to the [main page](./User_Guide.md)

Examples below follow the same pattern as those using [`curl`](./User_Guide_CLI.md). The `requests` library is recommended. Use Python shell to run the commands below, Jupyter Notebook or create and execute a `.py` file.

## Data Discovery

Import following two libraries, define the endpoints - authentication is not needed for metadata discovery on local docker deployment
```python
import requests
import json
import os

FDS_ENDPOINT="https://localhost:8443/federated-data-sharing/1.1.0"
```

> In development, insecure SSL connections warnings can safely be ignored. Change `verify=False` to `True` as required.

Make a call to the /dataset/list endpoint, then print the result dictionary:
```python
r = requests.get(f'{FDS_ENDPOINT}/datasets', verify=False)
dataset_list = r.json()
print(json.dumps(dataset_list, indent=4, sort_keys=True))
```

Choose 1st dataset for further exploration:
```python
dataset_1 = dataset_list['datasets'][0]['id']
```

Request first dataset catalogue by making a get call to /catalogue endpoint:
```python
r = requests.get(f'{FDS_ENDPOINT}/datasets/{dataset_1}/catalogue', verify=False)
catalogue = r.json()
print(json.dumps(catalogue, indent=4, sort_keys=True))
```

Request first dataset dictionary by making a get call to /dictionary endpoint:
```python
r = requests.get(f'{FDS_ENDPOINT}/datasets/{dataset_1}/dictionaries', verify=False)
dictionaries = r.json()
print(json.dumps(dictionaries, indent=4, sort_keys=True))
```
## Data Selection

Set the payload (Assuming you are in the top level folder of this project):
```python
file = open('./src/examples/example-query.graphql', 'r')
query = file.read()
```
Verify if the request is valid:
```python
headers = {'Content-type': 'plain/text', 'Accept': 'application/json' }
r = requests.post(f'{FDS_ENDPOINT}/selection/validate', data = query, headers=headers, verify=False)
valid = r.json() == 'True'
```
The response should be the simple JSON token `"True"` or `"False"`. 

Then if the request is valid, the selection can be made:
```python
headers = {'Content-type': 'plain/text', 'Accept': 'application/json' }
r = requests.post(f'{FDS_ENDPOINT}/selection/select', data = query, headers=headers, verify=False)
data = r.json()
```

## Tasks using federated computation

> TODO - pending updating the task API

## Next steps

- Back to the [main page](./User_Guide.md)
- Look at some [Worked examples](https://github.com/federated-data-sharing/common-api-examples)
