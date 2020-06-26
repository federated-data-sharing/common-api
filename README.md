# Federated Data Sharing Common API

## Introduction

This repository contains OpenAPI definitions for the Common API for Federated Data Sharing.

Currently, this is a work in progress reworking of the [Federated Data Sharing API](https://github.com/aridhia/federated-data-sharing) from the API.

This code is licensed under the [Mozilla Public License 2.0](https://www.mozilla.org/en-US/MPL/2.0/) see [LICENSE](./LICENSE)

## API Overview

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
