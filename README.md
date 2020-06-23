# Federated Data Sharing Common API

## Introduction

This repository contains OpenAPI definitions for the Common API for Federated Data Sharing.

Currently, this is a work in progress reworking of the [Federated Data Sharing API](https://github.com/aridhia/federated-data-sharing) from the API.

This code is licensed under the [Mozilla Public License 2.0](https://www.mozilla.org/en-US/MPL/2.0/) see [LICENSE](./LICENSE)

## API Overview

|Endpoint                           |HTTP   |Summary                                                    |
|:----------------------------------|:------|:----------------------------------------------------------|
|`/datasets`                        |`GET`  |Get a List of Datasets that can be Filtered                |
|`/datasets/{datasetid}/catalogue`  |`GET`  |Get Catalogue Entry (Metadata) for Dataset                 |
|`/datasets/{datasetid}/dictionary` |`GET`  |Get a Dataset dictionary                                   |
|`/selection/validate`              |`POST` |Validate a Given selection                                 |
|`/selection/beacon`                |`POST` |Get a Beacon (T/F) for a Specified Data selection          |
|`/selection/select`                |`POST` |Perform a Selection Operation on a Dataset                 |
|`/selection/preview`               |`POST` |Preview the Results of a Selection Operation on a Dataset  |
|`/selection/profile`               |`POST` |Get a Profile of a Selection Operation on a Dataset        |