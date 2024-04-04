import logging
from flask import g
from flask.views import MethodView
from flask_smorest import Blueprint
from flask_jwt_extended import get_jwt, jwt_required

from utils.decorators import access_pass
from controllers.auth.login_controller import LoginController
from controllers.auth.logout_controller import LogoutController
from controllers.auth.change_password import ChangePasswordController
from schemas.authentication import LoginUserSchema, ChangePasswordSchema


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


@blp.route("/change-password")
class ChangePassword(MethodView):

    @blp.arguments(ChangePasswordSchema)
    @jwt_required()
    def post(self, change_password_info):
        """Change password of the user."""

        new_password = change_password_info["new_password"]
        return ChangePasswordController().change_password(new_password)


@blp.route("/role")
class UserRole(MethodView):

    @jwt_required()
    def get(self):
        """Returns the role of the user."""

        token = get_jwt()
        return {
            "role": token["role"]
        }
