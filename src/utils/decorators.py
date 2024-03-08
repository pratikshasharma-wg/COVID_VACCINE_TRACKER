import functools

from flask_jwt_extended import (
    verify_jwt_in_request, 
    get_jwt, 
)
from flask_smorest import abort


from config.logs.logs import Logs
from config.prints.prints import Prints
from config.prompts.prompts import PromptsConfig
from config.queries.db_queries import DbConfig
from handlers.auth_handler import AuthHandler


def load_config(func):
    def function():
        # Load all config files
        DbConfig.load()
        PromptsConfig.load()
        Prints.load()
        Logs.load()
        func()

    return function


def access_pass(lst):

    def decorator(func):
    
        @functools.wraps(func)
        def wrap_func(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            jti = claims["jti"]
            if AuthHandler().check_token_in_db(jti):
                abort(401, message = "You are logged out! Please login again!")
            elif claims["role"] not in lst:
                abort(403, message = "Permission not granted!")
            elif claims["default_pwd_changed"] == 0:
                abort(403, message="Please change your default password!")
            elif claims.get("profile_updated") is False:
                abort(403, message="Please update your profile first!")
            else:
                return func(*args, **kwargs)
        
        return wrap_func
    
    return decorator
