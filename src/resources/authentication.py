import logging
from flask import g
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from schemas.authentication import LoginUserSchema
from controllers.auth.login_controller import LoginController


blp = Blueprint("login", __name__, description = "Login user")

logger = logging.getLogger(__name__)


@blp.route("/login")
class LoginUser(MethodView):

    @blp.arguments(LoginUserSchema)
    def post(self, user_info):
        """ Logs in a user"""

        logger.info(f"[{g.request_id}] hits /login endpoint")
        return LoginController().login_user(user_info)
