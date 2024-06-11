import os
import logging
from flask import Flask
from flask_cors import CORS


from database.database_operations import db
from app_config import (
    app_config, 
    jwt_handler,
    register_blueprint, 
    register_request_id,
    register_error_handlers 
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
        jwt_handler()
        register_blueprint()
        register_request_id()
        register_error_handlers()

    return app

app = create_app()
CORS(app)
