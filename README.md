# Federated Data Sharing Common API

## Introduction

This repository contains OpenAPI definitions for the Common API for Federated Data Sharing. The API was original developed to facilitate collaboration and trusted data sharing networks between trusted research environments and data repositories. 

The code is licensed under the [Mozilla Public License 2.0](https://www.mozilla.org/en-US/MPL/2.0/) see [LICENSE](./LICENSE). As more organisations are joining the effort, a new governance process will be established. In the meantime, please contact [Aridhia Informatics](https://www.aridhia.com/contact-our-team/) for more information.

## API overview

The federated data sharing API provides a set of endpoints required that provide a 'common' API to organisations wishing to participate in data sharing or federated analysis. There are three sections to the API:

- Metadata
- Selection
- Federated compute 

Note that the federated compute API section is being reviewed and will be added shortly.

The table below illustrates how different sections of the API could be opened up to support levels of sharing between a hub and a client (such as a user in a trusted Workspace).

| Mode     | Metadata                     | Selection & Filtering of record-level data          | Federated compute on record level data.                |
|:---------|:-----------------------------|:----------------------------------------------------|:-------------------------------------------------------|
| Level 0  | Can be queried and retrieved | Can be queried remotely and transferred to a client | Federation not required, computation happens at client |
| Level 1  | Can be queried and retrieved | Can be queried remotely and transferred to a client | Federation not required, computation happens at client |
| Level 2  | Can be queried and retrieved | Not permitted                                       | Containerised computations can be executed remotely with<br>selection query input, approved results returned  |

Features:

- The API is defined in an [Open API specification](api/common_api.yml)
- API endpoints should be authenticated using OAuth tokens (out of band for this version)
- Selections are defined in [GraphQL](https://graphql.org/) as an abstraction over querying

Details of each endpoint:

|Endpoint                                             |HTTP   |Summary                                                    |
|:----------------------------------------------------|:------|:----------------------------------------------------------|
|`/datasets`                                          |`GET`  |Get a list of datasets. Shows the list of all datasets available for querying. |
|`/datasets/{datasetid}/catalogue`                    |`GET`  |Get Catalogue entry (metadata) for dataset. Returns the metadata for a specified dataset (by dataset ID). |
|`/datasets/{datasetid}/dictionaries`                 |`GET`  |Get a list of dataset Dictionaries. Returns a list of field descriptions for each table within a specified dataset (by dataset ID). |
|`/datasets/{datasetid}/dictionaries/{tableid}`       |`GET`  |Get a single Dataset Dictionary for a specified table. Returns a set field descriptions for the specified table (by table ID) within a specified dataset (by dataset ID). |
|`/selection/validate`                                |`POST` |Validate a Given selection. With a simple GraphQL query, check whether the query is valid and corresponds to real fields at this location.  |
|`/selection/beacon`                                  |`POST` |Get a Beacon (T/F) for a Specified Data selection. With a simple Graph QL query, check which locations contain data relevant to a specific query. |
|`/selection/select`                                  |`POST` |Perform a Selection Operation on a Dataset. With a simple Graph QL query, returns the full selection of data in a JSON or .csv format. |
|`/selection/preview`                                 |`POST` |Preview the Results of a Selection Operation on a Dataset. With a simple Graph QL query, returns a small sample of the selection in a JSON or .csv format.  |
|`/selection/profile`                                 |`POST` |Get a profile of a selection operation on a dataset. Returns a set of metrics for the given selection operation  |
