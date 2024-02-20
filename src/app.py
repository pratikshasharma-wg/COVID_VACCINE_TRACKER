import logging
import shortuuid
from flask_smorest import Api
from flask import Flask, g
from flask_jwt_extended import JWTManager


from database.database_operations import db
from resources.users import blp as user_blp
from resources.vaccine import blp as vaccine_blp
from resources.dose_details import blp as dose_blp
from resources.authentication import blp as login_blp
from resources.profile import blp as profile_blp
from resources.approved_dose_info import get_blp, approve_blp
import os
current_directory = os.path.dirname(__file__)
FPATH = os.path.join(current_directory, 'logs.txt')


logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    level = logging.DEBUG,
                    filename = FPATH)

logger = logging.getLogger('app')


def create_app():

    app = Flask(__name__)
    app.config["API_TITLE"] = "COVID Vaccine Tracker"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    app.register_error_handler(Exception, lambda: ({"error": "something happened in server"}, 500))
    app.config["JWT_SECRET_KEY"] = "pratiksha"
    db.create_tables()

    api = Api(app)

    jwt = JWTManager(app)

    @app.before_request
    def generate_request_id():
        request_id = shortuuid.ShortUUID().random(length=15)
        g.request_id = request_id

    api.register_blueprint(login_blp)
    api.register_blueprint(user_blp)
    api.register_blueprint(dose_blp)
    api.register_blueprint(vaccine_blp)
    api.register_blueprint(profile_blp)
    api.register_blueprint(get_blp)
    api.register_blueprint(approve_blp)
    return app
    
app = create_app()
