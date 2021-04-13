# Background Concepts

> Back to the [main page](./User_Guide.md)

## History

Federated Analysis and data sharing is a strategy to network data platforms and users. See the [Origins](Origins.md) for some of the background to this specific design.

## Terminology

- site - a data repository implementing the API
- client - a user's programme interacting with the API
- container - a Docker container encapsulating the analysis or computation require

## High-level workflow

The Common API provides a standard interface for data sharing protocols to connect between a user or client programme and a site implementing the API. 

Once you have obtained credentials from a site, you interact using the protocol of the Common API. The protocol is very lightweight and clients (users) are free to call the API in any sequence but we expect the following typical sequence of events:

1. Discovering data by inspecting **metadata**
2. Defining field selections and filters to **select** 
3. Selecting data directly for centralised analysis or using federated **tasks** (computation) to process a selection
4. **Combining results** from analysing data at source to produce a final report (e.g. a chart).

## Understanding Federated sites

Sites are also free to implement the API as they wish but there are some conventions expected. We expect sites to implement in one of two modes:

- Level 1: users can connect to the API and select data which can be downloaded directly. This may be suitably de-identified:

    - metadata API - implemented, externally accessible
    - selection API - implemented, externally accessible
    - task API - not required

- Level 2: since data cannot be shared the selection API is not only the task API is exposed 

    - metadata API - implemented, externally accessible
    - selection API - implemented, only available within task protocol 
    - task API - implemented, externally accessible

For more details, see the [API Overview](./API_Overview.md)

> Note that in most cases you should expect the output of your computation to be "quarantined" and reviewed for disclosure risk or similar criteria by the data provider.

## Accessing the API

The API is a RESTful standard web-based programming interface, and the user can select whatever client language or tool that they want. We have tested using `curl`, `python` and `R` as well as graphical clients like Postman. We assume the user is familiar with programmatic access to [Web API](https://en.wikipedia.org/wiki/Web_API) endpoints.

We assume the user has been provided credentials to obtain a bearer token for API requests. The method for providing a token is not currently part of the specification but in a typical [OAuth](https://en.wikipedia.org/wiki/OAuth) model, a user is provided a client ID and client secret (password). Using those credentials, they call an API endpoint and obtain a token. This token is added as a header on subsequent calls. The token is intended to provide authentication AND authorisation. Sites are free to change the output of API calls based on what the individual user is authorised.

Examples below are provided in `R`, `python` and `curl` in a Linux environment or similar.

> Note that for simplicity and portability, code should be developed in Linux compatible environments.

## Next Steps

Understanding the [Key Payloads](./User_Guide_Key_Payloads.md) for API calls.