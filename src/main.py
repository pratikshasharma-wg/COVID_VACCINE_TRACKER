import logging
from flask import Flask
from flask_smorest import Api
from flask_jwt_extended import JWTManager

from resources.users import blp as user_blp
from resources.vaccine import blp as vaccine_blp
from resources.dose_details import blp as dose_blp
from resources.authentication import blp as login_blp


logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    level = logging.DEBUG,
                    filename = 'src\\config\\logs\\logs.txt')

logger = logging.getLogger('main')
   
    
if __name__ == "__main__":  

    app = Flask(__name__)
    app.config["API_TITLE"] = "COVID Vaccine Tracker"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    
    api = Api(app)
 
    app.config["JWT_SECRET_KEY"] = "pratiksha"
    jwt = JWTManager(app)

    api.register_blueprint(login_blp)
    api.register_blueprint(user_blp)
    api.register_blueprint(dose_blp)
    api.register_blueprint(vaccine_blp)

    app.run(debug=True, port=3024)