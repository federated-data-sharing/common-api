# Federated Data Sharing Common API

## Introduction

This repository contains OpenAPI definitions for the Common API for Federated Data Sharing. The API was original developed to facilitate collaboration and trusted data sharing networks between trusted research environments and data repositories. 

## Contributing

The code is licensed under the [Mozilla Public License 2.0](https://www.mozilla.org/en-US/MPL/2.0/) see [LICENSE](./LICENSE). 

The project was [originally](./doc/Origins.md) part of an international collaboration on sharing data in clinical research. We now welcome contributions from a wider community. As more organisations are joining the effort, a new governance process will be established. In the meantime, please contact the [maintainers of the repository](mailto:info@fds-api.org).

## API overview

The federated data sharing API provides a set of endpoints required that provide a 'common' API to organisations wishing to participate in data sharing or federated analysis. Features:

- The API is defined Open API specifications.
- API endpoints should be authenticated using OAuth tokens (out of band for this version)
- Selections are defined in [GraphQL](https://graphql.org/) as an abstraction over querying

There are three sections to the API:

| Section           | Repository                                                                            |
|:------------------|:--------------------------------------------------------------------------------------|
|Metadata           |[common-api-metadata](https://github.com/federated-data-sharing/common-api-metadata)   |
|Selection          |[common-api-selection](https://github.com/federated-data-sharing/common-api-selection) |
|Federated compute  |[common-api-tasks](https://github.com/federated-data-sharing/common-api-tasks)         |

For maximum flexibility each section of the Common API is defined in separate submodules and repositories. In this way, sites can implement combinations as required or desirable in their particular setting.The table below illustrates how different sections of the API could be opened up to support levels of sharing between a hub and a client (such as a user in a trusted Workspace).

| Mode     | Metadata                     | Selection & Filtering of record-level data          | Federated compute on record level data.                |
|:---------|:-----------------------------|:----------------------------------------------------|:-------------------------------------------------------|
| Level&nbsp;0  | Can be queried and retrieved | Can be queried remotely and transferred to a client | Federation not required, computation happens at client |
| Level&nbsp;1  | Can be queried and retrieved | Can be queried remotely and transferred to a client | Federation not required, computation happens at client |
| Level&nbsp;2  | Can be queried and retrieved | Not permitted                                       | Containerised computations can be executed remotely with<br>selection query input, approved results returned  |

Details of each endpoint:

|Endpoint                                             |HTTP   |Summary                                                    |
|:----------------------------------------------------|:------|:----------------------------------------------------------|
|`/datasets`                                          |`GET`  |Get a list of available datasets. Shows the list of all datasets available for querying. |
|`/datasets/{datasetid}`                              |`GET`  |Get Catalogue entry (metadata) and Dictionaries (field descriptions) for dataset. Returns the catalogue metadata and a list of field descriptions for a specified dataset (by dataset ID). |
|`/datasets/{datasetid}/catalogue`                    |`GET`  |Get Catalogue entry (metadata) for dataset. Returns the catalogue metadata for a specified dataset (by dataset ID). |
|`/datasets/{datasetid}/dictionaries`                 |`GET`  |Get Dictionaries (field descriptions) for dataset. Returns a list of field descriptions for each table within a specified dataset (by dataset ID). |
|`/datasets/{datasetid}/dictionaries/{tableid}`       |`GET`  |Get a single dataset Dictionary for a specified table. Returns a set field descriptions for the specified table (by table ID) within a specified dataset (by dataset ID). |
|`/selection/validate`                                |`POST` |Validate a given selection query. With a simple GraphQL query, check whether the query is valid and corresponds to real fields at this location.  |
|`/selection/beacon`                                  |`POST` |Get a Beacon (T/F) for a specified data selection. With a simple Graph QL query, check which locations contain data relevant to a specific query. |
|`/selection/select`                                  |`POST` |Perform a selection operation on a dataset. With a simple Graph QL query, returns the full selection of data in a JSON or .csv format. |
|`/selection/preview`                                 |`POST` |Preview the results of a selection operation on a dataset. With a simple Graph QL query, returns a small sample of the selection in a JSON or .csv format.  |
|`/selection/profile`                                 |`POST` |Get a profile of a selection operation on a dataset. Returns a set of metrics for the given selection operation.  |
|`/tasks/service-info`                                |`GET`  |Get service information about the service,such as storage details, resource availability, and other documentation|
|`/tasks`                                             |`GET`  |Get a list of of tasks for the current user|
|`/tasks`                                             |`POST` |Create a new task using a task specification (links a selection query and containerised computation task)|
|`/tasks/validate`                                    |`POST` |Validate a task specification|
|`/tasks/{task_id}`                                   |`GET`  |Get task details including status. If available, includes a link to the output of the task|

|`/tasks/{task_id}/cancel`                            |`POST` |Cancel a task|
|`/health_check`                                      |`GET`  |Get a health check of the service. |

For detailed examples, refer to the [User Guide](./doc/User_Guide.md)
