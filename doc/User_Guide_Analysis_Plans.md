# Analysis plans in a federated settings 

> Back to the [main page](./User_Guide.md)

## Getting started

As a scientist, statistician or data scientist, you may be used to developing scripts working directly with data - your `R` or `python` scripts can load the data directly, or maybe you're using a spreadsheet package or a statistical tool which wraps up the analysis plan for you. If you're using federated analysis this may not be an option for you - the data is held remotely. Your interaction with the data will be via the programming interface ("API") or a tool that uses it. Whereas you would normally expect a high degree of iteration (or "trial and error") when working with local data, you need to plan for a different form of iteration.

Data platforms that implement the Common API commit to helping reduce the friction of remote access in a number of ways intended to help you:

- Implementing a *standard* API, which means you don't have to keep learning new ways of getting metadata or processing their data
- Providing detailed and up-to-date metadata on data they share through the API, giving you enough detail to adapt your analysis to what data is really there
- Letting you run *your* code on the data through the use of [docker containers](https://www.docker.com/resources/what-container)
- Supporting iterative sessions - where you can run your analysis as often as needed to answer your research questions (within some fair usage limits)

In return, you should revisit your analysis plan and structure it to the remote arrangement. You may want to consider:

- whether you will be interacting with one or more than one remote site (also known as a "node") 
- whether you will be interacting with a mix of nodes at different levels of sharing (also known as "Level 0", "Level 1" or "Level 2" nodes)
- setting a number of stages or phases for your analysis in order to get early feedback on the process and build trust in the data and your connection with the remote sites.
- whether integrating data from multiple sources is important for your analysis algorithm (for example to develop a machine learning model)

Examples of staging or phasing analysis might reflect a standard research or data science life cycle:

- exploratory analysis: systematically validating, summarising or exploring the remote data early on in orde
- quality checks, outlier analysis
- sampling
- visualisation
- data engineering or integration (or at least creating a standard data frame for analysis)
- statistical tests
- modelling data
- validating models

A modular and composable approach to your analysis code will allow you to iterate at each stage and if necessary combine the analysis into reproducible process. This should reduce frustrations with not having direct access to data.

## Defining a selection

All remote sites must provide field level metadata for data you have access to. This allows you to define a selection query. In a simple example this could define:

- what table you want to read from
- what fields within the table you want to analyse

Selections are defined using a standard called [GraphQL](https://graphql.org/). With this you can express a selection in relatively simple terms.

For example, we can imagine a table called `virtual_cohort` with fields that include `family_history` (of a disease like Alzheimer's), `age` (in years) and `apoe` (a biomarker for the disease). If you just wanted to to analyse `age` and `apoe` the selection would look like this:
```
{
    virtual_cohort {
        age
        apoe
    }
}
```
More details of how define GraphQL queries can be found on the [community pages](https://graphql.org/learn/) - bear in mind for this use case, we only need to know about selection *queries* and can ignore schemas and mutations.



## Next steps

Understand [Containerising scripts](./User_Guide_Containerising_Tasks.md)