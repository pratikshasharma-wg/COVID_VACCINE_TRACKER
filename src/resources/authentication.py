import logging
from flask import g
from flask.views import MethodView
from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required

from schemas.authentication import LoginUserSchema
from controllers.auth.login_controller import LoginController
from controllers.auth.logout_controller import LogoutController


blp = Blueprint("auth", __name__, description = "Login user")

logger = logging.getLogger(__name__)


@blp.route("/login")
class LoginUser(MethodView):

    @blp.arguments(LoginUserSchema)
    def post(self, user_info):
        """ Logs in a user"""

        logger.info(f"[{g.request_id}] hits /login endpoint")
        return LoginController().login_user(user_info)
    

@blp.route("/logout")
class LogoutUser(MethodView):

    @jwt_required()
    def post(self):
        """Logout the user."""

        logger.info(f"{[g.request_id]} user logged out!")
        return LogoutController().logout_user()
