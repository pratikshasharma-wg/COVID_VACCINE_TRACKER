import os
import logging
from flask import Flask

from database.database_operations import db
from app_config import (
    app_config, 
    register_blueprint, 
    register_error_handlers, 
    register_request_id, 
    jwt_handler
)


current_directory = os.path.dirname(__file__)
FPATH = os.path.join(current_directory, 'logs.txt')


logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    level = logging.DEBUG,
    filename = FPATH
)

logger = logging.getLogger('app')


def create_app():

    db.create_tables()
    app = Flask(__name__)
    with app.app_context():
        app_config()
        register_blueprint()
        register_request_id()
        register_error_handlers()
        jwt_handler()

    return app
