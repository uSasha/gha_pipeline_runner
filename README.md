Here is an attempt to use GH Actions as a rudimentary SAAS pipelines runner

For details check the `./.github/workflows/run_pipelines.yml` file.
The first job `collect_branches` will get active branches from external API and create build matrix JSON.
The second job `execute_branches` will run multiple times with the name of the branch passed to the docker 
container as ENV variable, so here is a way to set different config, etc.

[Here](https://github.com/uSasha/gha_dag_runner/actions/runs/781111060) is an example of multipipelines run.
