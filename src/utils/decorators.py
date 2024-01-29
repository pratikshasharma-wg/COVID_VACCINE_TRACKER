import logging
import functools
from config.logs.logs import Logs
from config.prints.prints import Prints
from config.prompts.prompts import PromptsConfig
from config.queries.db_queries import DbConfig
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from flask_smorest import abort


def load_config(func):
    def function():
        # Load all config files
        DbConfig.load()
        PromptsConfig.load()
        Prints.load()
        Logs.load()
        func()

    return function


def role_required(lst):

    def decorator(func):
    
        @functools.wraps(func)
        def wrap_func(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims["role"] in lst:
                return func(*args, **kwargs)
            else:
                abort(400, message = "Permission not granted!")
        
        return wrap_func
    
    return decorator