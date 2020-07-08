# User Guide

## Introduction

The main purpose of the  Federated Data Sharing Common API is to support analysis of multiple data sets while allowing a data owner (custodian, controller) to control how data is exposed to the analysis. See the [Origins](Origins.md) for some of the background to this design. 

The provides a standard interface for data sharing protocols to connect between a user or client programme and a site implementing the API. The protocol is very light weight now and clients (users) are free to call the API in any sequence but we expect the following typical sequence of events: 

1. Discovering data by inspecting **metadata**
2. Defining field selections and filters to **select** 
3. Selecting data directly for centralised analysis or using federated **tasks** (computation) to process a selection
4. **Combining results** from analysing data at source to produce a final report (e.g. a chart).

## Implementation options

Sites are also free to implement the API as they wish but there are some conventions expected. We expect sites to implement in one of two modes:

- Level 1: users can connect to the API and select data which can be downloaded directly. This may be suitably de-identified:

    - metadata API - implemented, externally accessible
    - selection API - implemented, externally accessible
    - task API - not required

- Level 2: since data cannot be shared the selection API is not only the task API is exposed 

    - metadata API - implemented, externally accessible
    - selection API - implemented, only available within task protocol 
    - task API - implemented, externally accessible

## Terminology

- site - a data repository implementing the API
- client - a user's programme interacting with the API
- container - a Docker container encapsulating 

## Accessing the API

The API is a RESTful standard web-based programming interface, and user can select whatever client language or tool that they want. We have tested using `curl`, `python` and `R` as well as graphical clients like Postman. We assume the user is familiar with programmatic access to [Web API](https://en.wikipedia.org/wiki/Web_API) endpoints.

We assume the user has been provided credentials to obtain a bearer token for API requests. The method for providing a token is not currently part of the specification but in a typical [OAuth](https://en.wikipedia.org/wiki/OAuth) model, a user is provided client ID and client secret (password). Using those credentials, they call an API endpoint and obtain a token. This token is added as a header on subsequent calls. The token is intended to provide authentication AND authorisation. Sites are free to change the output of API calls based on what the individual user is authorised.

Examples below are provided in `R`, `python` and `curl` in a Linux environment or similar.

## Key payloads

The metadata API is a read-only API to discover and navigate what data might be available at a site. The API uses specific payloads to define tasks or selections. These can be constructed programmatically or in files passed to commands and libraries.

Selections are currently defined in [GraphQL](https://graphql.org/) and posted with `Content-type: plain-text`. This was chosen to abstact from specific query languages like SQL or RDF and to leverage a wider range of underlying data management technologies. A selection query is defined using GraphQL [queries](https://graphql.org/learn/queries/). Broadly speaking the structure for a query selection of fields `field1`, `field2` and `field3` fom the table `table_name` the GraphQL would look like:

```
{
    table_name {
        field1
        field2
        field3
    }
}
```

Tasks are currently specified in a variant of the GA4GH [Task Execution Service](https://github.com/ga4gh/task-execution-schemas). We expect closer alignment by Version 1.0. A task specification is a JSON object, with a selection query embedded:

> TODO: This payload specification is being reviewed at the time of writing.

```json
{
    "name":        "MD5 example",
    "description": "Task which runs md5sum on the input file.",
    "tags": {
      "custom-tag": "tag-value"
    },
    "inputs": [
      {
        "content": "{table_name { field1 field2 field3 }}"
      }
    ],
    "outputs" : [
      {
        "url" :  "/path/to/output_file",
        "path" : "/mnt/output/"
      }
    ],
    "resources" : {
      "cpuCores": 1,
      "ramGb":    1.0,
      "diskGb":   100.0,
      "preemptible": false
    },
    "executors" : [
      {
        "image" : "container_registry:image-aname:version_no",
        "command" : ["entrypoint", "/container/input"],
        "stdout" : "/mnt/logs/stdout",
        "stderr" : "/mnt/logs/stderr",
        "workdir": "/tmp"
      }
    ]
}
```

The structure of the JSON is:

| Property                  | Specification                                                     |
|:--------------------------|:------------------------------------------------------------------|
| name                      | A short name for the task; does not need to be unique             |
| description               | A short description of the what the task is                       |
| inputs/content            | The GraphQL selection query                                       |
| outputs/path              | Key outputs
| executors/image           | The URL of a container image (in an approved registry)            |
| resources                 | Not enforced now but estimates the compute resources for the task |

A task can assume that inputs are provided in the `/mnt/input` folder attached to their container, wheres outputs can be written to `/mnt/output`. Logs may be delivered to `/mnt/logs`.

## Command line - using curl and jq

Using `curl` and `jq` on the command line is a low level way to interact with the API in shell scripts.

We assuming the API is accessible at an endpoint `FDS_ENDPOINT`. For example, if you run the reference implementation, this will be:

```sh
FDS_ENDPOINT="https://localhost:8443/federated-data-sharing/1.1.0"
```

We use `curl_opts` to set some useful options. For example in the reference implementation the certificate (for `https`) is self-signed so should not be checked. Set this option:

```sh
curl_opts="-k"
```

To get a token, use the endpoint provided by the site. For example, the following is an example of how to retrieve a token

```sh
token=`curl $curl_opts --user "$API_USER:$API_PASS"\
     -d grant_type=client_credentials -X POST\
     "$FDS_ENDPOINT/auth/connect/token" | jq -r '.access_token'`
```

### Data Discovery

From there get a list of datasets:
```sh
curl $curl_opts -H "Authorization: Bearer $token"\
     -H "Accept: application/json"\
     "$FDS_ENDPOINT/datasets" | jq
```

To pick the first dataset:
```sh
dataset_id=`curl $curl_opts -X GET -H "Accept: application/json"\
       "$FDS_ENDPOINT/datasets"\
        | jq -r '.datasets[] | .id' | head -1`
echo $dataset_id
```

You can then get the catalogue for that dataset...
```sh
curl $curl_opts -X GET -H "Accept: application/json"\
        "$FDS_ENDPOINT/datasets/$dataset_id/catalogue" | jq
```

... and then get the dictionary for that dataset - not that there may multiple 'tables' within the dataset, with individual dictionaries.
```sh
curl $curl_opts -X GET -H "Accept: application/json"\
     "$FDS_ENDPOINT/datasets/$dataset_id/dictionaries"\
      | jq -r '.dictionaries[].id'
```

### Data Selection

Selection currently uses [GraphQL](https://graphql.org/) as a format for defining selections and filters on data. An example is provided in [src/examples/example-query.graphql](src/examples/example-query.graphql). This is intended as an abstraction from underlying query mechanisms such as SQL.

The API is intended to be incremental: a user can define a query based on the data discovery stage. This query can be validated, then executed to different levels. The API may be implemented to support different levels or none (if Federated compute is the only approved method for selection and analysis).

To validate a query such as the example query provided, we can post the JSON body: 
```sh
curl $curl_opts -X POST\
     -H "Authorization: Bearer $token" -H "Accept: application/json"\
     -H  "Content-Type: text/plain" --data @src/examples/example-query.graphql\
     "$FDS_ENDPOINT/selection/validate" | jq
```

To then select using that same query:
```sh
curl $curl_opts -X POST\
     -H "Authorization: Bearer $token" -H "Accept: application/json"\
     -H  "Content-Type: text/plain" --data @src/examples/example-query.graphql\
     "$FDS_ENDPOINT/selection/select" | jq
```
The other endpoints `/selection/beacon`, `/selection/preview`, `/selection/profile` work in the same way. 

### Tasks using federated computation

> TODO - pending updating the task API

## Using Python


Examples below follow the same pattern as those using `curl` above. The `requests` library is recommended. Use Python shell to run the commands below, Jupyter Notebook or create and execute a `.py` file.

### Data Discovery

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
### Data Selection

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
## Using R

For R interacting with an API, the [`httr`](https://httr.r-lib.org/) library is recommended. This can be done interactively, or in an `.R` script. The examples below are at an R console prompt (`>`). The [tidyverse libraries](https://www.tidyverse.org/) and related libraries for processing JSON are recommended and used in the examples below.

For these examples, R 3.6.1 was used, with the following dependencies installed:
```R

```

Set up the library dependency and define the end point.
```R
library(tidyverse)
library(jsonlite)
library(httr)
library(purrr)
library(stringr)
library(readr)
library(httr)
FDS_ENDPOINT <- "https://localhost:8443/federated-data-sharing/1.1.0"
```
If your implementation has a self-signed certificate, temporarily disable SSL warnings with:
```R
httr::set_config(httr::config(ssl_verifypeer=0L, ssl_verifyhost=0L))
```

### Access tokens

If the end point requires an acess token (note the reference implementation does not) obtain an access token. This example may vary by endpoint but with OAuth2 normally this involves the following parameters that are provided by the endpoint provider.

- grant_type
- client_id
- client_secret

> Handling JSON in R can be awkward so the examples below take a case-by-case approach to parsing responses from JSON to useful data structures for use in R.

```R
> TOKEN_ENDPOINT <- 'AS PROVIDED'
> GRANT_TYPE <- 'AS PROVIDED'
> CLIENT_ID <- 'AS PROVIDED'
> CLIENT_SECRET <- 'AS PROVIDED'
> r <- POST(TOKEN_ENDPOINT,
          body=list(grant_type=GRANT_TYPE),
          authenticate(CLIENT_ID, CLIENT_SECRET)
> response <- content(r, 'parsed')
> access_token <- response$access_token
```

> Note: The access token may need to be refreshed from time to time.

In what follows, if you have a token, add the following to `GET` and `POST` calls:
```R
add_headers(Authorization=paste('Bearer', access_token, sep=" "))
```
### Examples: Data Discovery

To get the dataset list using an `httr` `GET()` call:
```R
r <- GET(paste0(FDS_ENDPOINT, '/datasets'))
resp <- content(r, 'parsed')
dataset_list <- map(resp$datasets, 'id')
```

To obtain the dictionary for a dataset `dataset_id`:
```R
r <- GET(paste0(FDS_ENDPOINT, '/datasets/', dataset_id, '/dictionaries'))
resp <- content(r, 'text', encoding='UTF-8')
dictionaries <- fromJSON(resp, flatten=TRUE)
```
### Examples: Data selection

To validate a query:
```R 
r <- POST(paste0(FDS_ENDPOINT, '/selection/validate'),
        body=upload_file('src/examples/example-query.graphql'), 
        encode='raw')
resp <- content(r, 'parsed')
validation <- resp$success
```

> Note: 'raw' implies plain text

To submit the query:
```R 
r <- POST(paste0(FDS_ENDPOINT, '/selection/select'),
        body=upload_file('src/examples/example-query.graphql'), 
        add_headers('Accept'='application/json'),
        encode='raw')
resp <- content(r)
```
In this worked example, the data is accessible via `resp$data$synthetic_alzheimers_profile`

### Tasks using federated computation

> TODO - pending updating the task API