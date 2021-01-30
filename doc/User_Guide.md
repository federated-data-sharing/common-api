# User Guide

> Back to the main [README](../README.md)

## Contents

- Introduction - this file
- [Background_Concepts](./User_Guide_Background.md)
- Understanding [Analysis plans](./User_Guide_Analysis_Plans.md) in a federated setting
- [Containerising scripts](./User_Guide_Containerising_Tasks.md)
- [Key Payloads](./User_Guide_Key_Payloads.md)
- [Command Line](./User_Guide_CLI.md) - e.g. with `curl`
- [Python](./User_Guide_Python.md)
- [R](./User_Guide_R.md)

A separate repository provides [Worked examples](https://github.com/federated-data-sharing/common-api-examples)

## Introduction

The main purpose of the  Federated Data Sharing Common API is to support analysis of multiple data sets while allowing a data owner (custodian, controller) to control how data is exposed to the analysis. A set of APIs allow users to query metadata, select data and perform computation on data held remotely. This is intended to support a cycle where you can:

- get field-level type and content metadata for remote data
- define a selection (pick fields) or filter (pick rows) you want to analyse
- execute some computation on the selection

In Level 1 federated data sharing, you may have access to select row level data whereas in Level 2 you will only be able to specify your selection and computation task and have both executed remotely. This means that your analysis plan needs to adapt to the protocol.

## Next steps

Understand the [Background concepts](./User_Guide_Background.md) to enable you to use the API effectively.