import shortuuid
from flask import g
from flask_smorest import Api
from flask_jwt_extended import JWTManager

from utils.exceptions import FailedValidation
from resources.users import blp as user_blp
from resources.dose_details import blp as dose_blp
from resources.authentication import blp as login_blp
from resources.vaccine import blp as vaccine_blp
from resources.profile import blp as profile_blp
from resources.approved_dose_info import approve_blp, get_blp

from flask import current_app as app


def app_config():
    app.config["API_TITLE"] = "COVID Vaccine Tracker"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["JWT_SECRET_KEY"] = "pratiksha"


def register_blueprint():
    api = Api(app)
    api.register_blueprint(login_blp)
    api.register_blueprint(user_blp)
    api.register_blueprint(dose_blp)
    api.register_blueprint(vaccine_blp)
    api.register_blueprint(profile_blp)
    api.register_blueprint(get_blp)
    api.register_blueprint(approve_blp)


def register_request_id():
    @app.before_request
    def generate_request_id():
        request_id = shortuuid.ShortUUID().random(length=15)
        g.request_id = request_id


def register_error_handlers():
    app.register_error_handler(Exception, lambda: ({"error": "something happened in server"}, 500))
    app.register_error_handler(FailedValidation, lambda error: ({error.dump(), error.code}))


def jwt_handler():
    jwt = JWTManager(app)
    
    @jwt.expired_token_loader
    def on_expired_token():
        return {
            'message': 'Your token has expired!'
        }, 401
    
    @jwt.invalid_token_loader
    def on_invalid_token():
        return {
            'message': 'Invalid token!'
        }, 401
