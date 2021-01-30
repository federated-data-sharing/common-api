## Key payloads

> Back to the [User Guide](./User_Guide.md)

The metadata API is a read-only API to discover and navigate what data might be available at a site. The API uses specific payloads to define tasks or selections. These can be constructed programmatically or in files passed to commands and libraries.

Selections are currently defined in [GraphQL](https://graphql.org/) and posted with `Content-type: plain-text`. This was chosen to abstact from specific query languages like SQL or RDF and to leverage a wider range of underlying data management technologies. A selection query is defined using GraphQL [queries](https://graphql.org/learn/queries/). Broadly speaking the structure for a query selection of fields `field1`, `field2` and `field3` fom the table `table_name` the GraphQL would look like:

```
{
    table_name {
        field1
        field2
        field3
    }
}
```

Tasks are currently specified in a variant of the GA4GH [Task Execution Service](https://github.com/ga4gh/task-execution-schemas). We expect closer alignment by Version 1.0. A task specification is a JSON object, with a selection query embedded:

> TODO: This payload specification is being reviewed at the time of writing.

```json
{
    "name":        "MD5 example",
    "description": "Task which runs md5sum on the input file.",
    "tags": {
      "custom-tag": "tag-value"
    },
    "inputs": [
      {
        "content": "{table_name { field1 field2 field3 }}"
      }
    ],
    "outputs" : [
      {
        "url" :  "/path/to/output_file",
        "path" : "/mnt/output/"
      }
    ],
    "resources" : {
      "cpuCores": 1,
      "ramGb":    1.0,
      "diskGb":   100.0,
      "preemptible": false
    },
    "executors" : [
      {
        "image" : "container_registry:image-aname:version_no",
        "command" : ["entrypoint", "/container/input"],
        "stdout" : "/mnt/logs/stdout",
        "stderr" : "/mnt/logs/stderr",
        "workdir": "/tmp"
      }
    ]
}
```

The structure of the JSON is:

| Property                  | Specification                                                     |
|:--------------------------|:------------------------------------------------------------------|
| name                      | A short name for the task; does not need to be unique             |
| description               | A short description of the what the task is                       |
| inputs/content            | The GraphQL selection query                                       |
| outputs/path              | Key outputs
| executors/image           | The URL of a container image (in an approved registry)            |
| resources                 | Not enforced now but estimates the compute resources for the task |

A task can assume that inputs are provided in the `/mnt/input` folder attached to their container, wheres outputs can be written to `/mnt/output`. Logs may be delivered to `/mnt/logs`.

## Next Step

Understanding [Analysis plans](./User_Guide_Analysis_Plans.md) in a federated setting

Try the API using:

- [Command Line](./User_Guide_CLI.md) tools - e.g. with `curl`
- [Python](./User_Guide_Python.md)
- [R](./User_Guide_R.md)
