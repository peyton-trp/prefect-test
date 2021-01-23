"""General utils
"""
import cloudpickle
import logging
import prefect

LOGGING_LOCATION = "dog.log"

def set_logger():
    """Adds a filehandler to prefect's root logger

    Returns
    -------
    logging.Logger
        Prefect root logger + filehandler, or new logger with file handler if prefect logger
        modification if prefect logger modification fails
    """
    try:
        root_logger = prefect.utilities.logging.get_logger()

        formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(name)s | %(message)s")
        fh = logging.FileHandler(LOGGING_LOCATION)

        fh.setFormatter(formatter)
        root_logger.addHandler(fh)

        root_logger.info("Prefect root logger successfully configured with file handler")

        return root_logger

    except Exception as e:

        logger = logging.getLogger("alternative_logger")

        formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(name)s | %(message)s")
        fh = logging.FileHandler(LOGGING_LOCATION)

        fh.setFormatter(formatter)
        logger.addHandler(fh)

        logger.error("Failed to add file handler to root logger for prefect, returning alternative logger")
        logger.error(e)

        return logger

def unpickle_prefect_res(path: str):

    with open(path, "rb") as f:
        content = f.read()
        res = cloudpickle.loads(content)

        return res