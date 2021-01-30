# Using R

> Back to the [main page](./User_Guide.md)

## Getting Started

For R interacting with an API, the [`httr`](https://httr.r-lib.org/) library is recommended. This can be done interactively, or in an `.R` script. The examples below are at an R console prompt (`>`). The [tidyverse libraries](https://www.tidyverse.org/) and related libraries for processing JSON are recommended and used in the examples below.

For these examples, R 3.6.1 was used, with the following dependencies installed:

- [tidyverse](https://www.tidyverse.org/) including purrr, stringr and readr
- [jsonlite](https://www.rdocumentation.org/packages/jsonlite)
- [httr](https://httr.r-lib.org/)

Set up the library dependency and define the end point.
```R
library(tidyverse)
library(jsonlite)
library(httr)
library(purrr)
library(stringr)
library(readr)
FDS_ENDPOINT <- "https://localhost:8443/federated-data-sharing/1.1.0"
```
If your implementation has a self-signed certificate, temporarily disable SSL warnings with:
```R
httr::set_config(httr::config(ssl_verifypeer=0L, ssl_verifyhost=0L))
```

## Access tokens

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
## Data Discovery

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

## Data selection

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

## Tasks using federated computation

> TODO - pending updating the task API

## Next steps

- Back to the [main page](./User_Guide.md)
- Look at some [Worked examples](https://github.com/federated-data-sharing/common-api-examples)
