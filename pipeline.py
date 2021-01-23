"""Main pipeline to be run for data processing
"""
import os

from config_vars import password

print(f"Checkpointing: {os.getenv('PREFECT__FLOWS__CHECKPOINTING')}")
from pathlib import Path

from pipeline_tasks import cat, dog, sql_task
from prefect import Flow
from utils import set_logger

logger = set_logger()


with Flow("DOG_FLOW") as f:

    # data = get_data()
    # clean_df = clean_dataframe(data)
    # updated_values = update_values(clean_df)

    # write_data(updated_values)

    logger.warning("!!!!!!!!!!!!!!1")

    d = dog()

    c = cat(d)

    logger.warning("???????????")

    s = sql_task(password=password)


# f.register(project_name="test flow")
f.run()





# f.visualize()
# logger.info(state.result[s].result)
# print(state.result[s].result)
