#--------------------------------------------------------------
# Imports
#--------------------------------------------------------------
from prefect import Flow, task, Parameter
from prefect.run_configs import LocalRun
from prefect.storage import GitHub
import prefect
from prefect.engine.results import LocalResult
from prefect.tasks.sql_server import SqlServerFetch
from prefect.tasks.secrets import EnvVarSecret
#--------------------------------------------------------------
# Setup
#--------------------------------------------------------------

result_formatter = LocalResult(
    dir=prefect.config.STORAGE_PATH,
    location="{flow_name}/"
    "{scheduled_start_time:%d-%m_%H-%M-%S}/"
    "{task_full_name}-{task_run_id}.prefect_result")

#--------------------------------------------------------------
# Custom task functions
#--------------------------------------------------------------
@task(name="dog", result=result_formatter)
def dog(thing):
    logger = prefect.context.get("logger")
    logger.info(thing)
    return "This is a returned string"

@task(name="view sql")
def view_sql(sql):
    logger = prefect.context.get("logger")
    logger.info(sql)
#--------------------------------------------------------------
# Task classes
#--------------------------------------------------------------
get_manual_override_rows = """
--sql
SELECT * from manual_override
WHERE yes_no = 'yes'
and text != 'No text - category selected manually';
"""

# Get our database items
sql_task = SqlServerFetch(
        db_name=prefect.config.sql_server.database,
        user=prefect.config.sql_server.user,
        host=prefect.config.sql_server.server,
        query=get_manual_override_rows,
        fetch='many',
        fetch_count=3,
        result=result_formatter,
        name="SQL-stuff"
        # commit: bool = False,
)
#--------------------------------------------------------------
# Flow context
#--------------------------------------------------------------
with Flow("github_flow") as f:

    password = EnvVarSecret(prefect.config.sql_server.password_var)

    logger = prefect.context.get("logger")
    thing = Parameter("thing", default=["Thing 1"])
    d = dog(thing)

    s = sql_task(password=password)

    v = view_sql(s)

#--------------------------------------------------------------
# Closing Details
#--------------------------------------------------------------
f.run_config = LocalRun(
    env={
        "PREFECT__USER_CONFIG_PATH": '/Users/peytonrunyan/TRP/prefect/config.toml'})

f.storage = GitHub(
    repo="peyton-trp/prefect-test",
    path="pipeline.py",
    secrets=["GITHUB_ACCESS_TOKEN"]
)

f.register("cat_flow")