"""Where all of the tasks for our pipeline go
"""
from pathlib import Path

import prefect
from config_vars import db_name, host, user, result_folder
from prefect import task
from prefect.engine.results import LocalResult
from prefect.tasks.sql_server import SqlServerFetch
from sql import get_manual_override_rows

path = Path(__file__).resolve().parent / result_folder

result_formatter = LocalResult(
    dir=path,
    location="{flow_name}/"
    "{scheduled_start_time:%d-%m_%H-%M-%S}/"
    "{task_full_name}-{task_run_id}.prefect_result")


# Get our database items
sql_task = SqlServerFetch(
        db_name=db_name,
        user=user,
        host=host,
        query=get_manual_override_rows,
        fetch='many',
        fetch_count=3,
        result=result_formatter,
        name="SQL-stuff"
        # commit: bool = False,
)

# create a demo task
@task
def clean_dataframe(df):

    df = df[df[column] == some_item].filter(something)

    return df

# Return length of string
@task(name="puppy", result=result_formatter)
def dog():
    logger = prefect.context.get("logger")
    logger.info("*********************")
    res = len("dog")
    return "This is a returned string"


# Print length of string
@task(result=result_formatter)
def cat(i: int, result=LocalResult(dir=path)):
    logger = prefect.context.get("logger")
    logger.debug(i)
    return "nine lives"
