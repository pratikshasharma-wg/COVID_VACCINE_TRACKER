import logging
import functools
from config.logs.logs import Logs
from config.prints.prints import Prints
from config.prompts.prompts import PromptsConfig
from config.queries.db_queries import DbConfig


def load_config(func):
    def function():
        # Load all config files
        DbConfig.load()
        PromptsConfig.load()
        Prints.load()
        Logs.load()
        func()
    return function

