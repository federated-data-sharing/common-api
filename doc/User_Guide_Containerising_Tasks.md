# Containerising a script as a federated compute task

> Back to the [main page](./User_Guide.md)

## Getting started

In order to execute a remote computation task, your analysis code must be packaged up in a docker container. 

> For simplicity we use the word "script" for this code as this is common data science but your could be anything that is containerised including complex programmes with library or package dependencies all encapsulated within the container.

## Workflow

In order to containerise the script, it is recommended to go through the following steps:

1. Run the script on dummy or synthetic data on the command line on your local machine
2. Package up the script in a container and run using local docker installation, via command line on your local machine
3. Run the containerised script on one or more remote site via Federated Data Sharing API

![Developing a containerised script](./sketch_process.jpg)

A set of conventions set out how you should expect inputs to your containers or outputs of your computation to be handled. In the base, simple case your script should *read* one or more input CSV files corresponding to your selection query from a specified folder (`/mnt/input`) which may be read-only. Your script is then able to *write* one or more files to a specified folder (`/mnt/ouput`).

![Reading and writing from the container](./sketch_docker.jpg)

When running a federated task in a more complex scenario, the same container might be used across multiple sites, or a selection filter might process only some of the data available at a given site. When combining data, it is useful to consider what 'post-processing' produces the final output you require:

![Overview](./sketch_full.jpg)

## Next steps

Try the API using:

- [Command Line](./User_Guide_CLI.md) tools - e.g. with `curl`
- [Python](./User_Guide_Python.md)
- [R](./User_Guide_R.md)
