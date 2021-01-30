# Command line - using curl and jq

> Back to the [main page](./User_Guide.md)

## Getting started

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

## Data Discovery

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

## Data selection

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

## Next steps

- Back to the [main page](./User_Guide.md)
- Look at some [Worked examples](https://github.com/federated-data-sharing/common-api-examples)
