# API overview

> Back to the main [README](../README.md)

## Overview

The federated data sharing Common API establishes an open standard for data platforms to participate in a open and closed data sharing networks. It speciies a set of endpoints required that provide a 'common' API to organisations wishing to participate in data sharing or federated analysis. Data sharing agreements are diverse and we need to remove barriers for data sharing amongst data controllers. This approach is intended to:

- Clarity and transparency of the model in a complex ecosystem
- Accelerate availability of data for research
- Devolve the decision-making and governance to the appropriate level.
- Encourage convergence of existing (proprietary or niche) efforts
- Encourage an ecosystem of tools & syndication

By adopting the API, a data provider and their network can implement “connector” layer once, join multiple networks. Our approach asks data controllers to self-select at what ‘level‘ they can join the network, mainly dependent on what they are permitted to do with data in their custody:

| Mode          | Metadata                     | Selection & Filtering of record-level data          | Federated compute on record level data.                |
|:--------------|:-----------------------------|:----------------------------------------------------|:-------------------------------------------------------|
| Level&nbsp;0  | Can be queried and retrieved | Can be queried remotely and transferred to a client | Federation not required, computation happens at client |
| Level&nbsp;1  | Can be queried and retrieved | Can be queried remotely and transferred to a client | Federation not required, computation happens at client |
| Level&nbsp;2  | Can be queried and retrieved | Not permitted                                       | Containerised computations can be executed remotely with<br>selection query input, approved results returned  |

## Open Standards

Rather than reinventing the wheel, the Common API **adopts and adapts** existing standards efforts 

- The API is defined Open API specifications.
- API endpoints should be authenticated using OAuth tokens (out of band for this version)
- Descriptive metadata is defined in a variant of the [W3C DCAT](https://www.w3.org/TR/vocab-dcat-2/) standard and a simple data dictionary model.
- Selections are defined in [GraphQL](https://graphql.org/) as an abstraction over querying, selection and filtering
- Federated computations are defined in a variant of the [GA4GH Task Execution Service (TES) API](http://ga4gh.github.io/task-execution-schemas/) 

> Note: Field-level metadata (data dictionaries) are defined in a simple, pragmatic data model - existing partners aim to define or adopt a more robust community standard. 

## API modularity

There are three sections to the API:

| Section           | Repository                                                                            | Level 0 | Level 1 | Level 2 |
|:------------------|:--------------------------------------------------------------------------------------|---------|---------|---------|
|Metadata           |[common-api-metadata](https://github.com/federated-data-sharing/common-api-metadata)   | Yes     | Yes     | Yes     |
|Selection          |[common-api-selection](https://github.com/federated-data-sharing/common-api-selection) | N/A     | Yes     | Yes **  |
|Federated compute  |[common-api-tasks](https://github.com/federated-data-sharing/common-api-tasks)         | N/A     | N/A     | Yes     |

> \*\* Level 2 sites must implement the selection API "behind the scenes" to provide compute tasks with the selection required.

For maximum flexibility each section of the Common API is defined in separate git submodules and repositories. In this way, sites can implement combinations as required or desirable in their particular setting.The table below illustrates how different sections of the API could be opened up to support levels of sharing between a hub and a client (such as a user in a trusted Workspace).

## Endpoints

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
