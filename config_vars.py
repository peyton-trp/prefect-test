"""Generate config variables here
"""
import os
from configparser import ConfigParser
from dotenv import load_dotenv

config = ConfigParser()    # pylint: disable=C0103
config.read("config.ini")
load_dotenv()

# database
db_type = 'HUB'

db_name = config[db_type]['database']
user = os.getenv(config[db_type]['username'])
host = config['ALL']['server']
password = os.getenv(config[db_type]['password'])

# prefect
os.environ["PREFECT__FLOWS__CHECKPOINTING"] = config['PREFECT']['checkpointing']
os.environ["PREFECT__LOGGING__LEVEL"] = config['PREFECT']['logging_level']
result_folder = config["PREFECT"]["result_folder"]