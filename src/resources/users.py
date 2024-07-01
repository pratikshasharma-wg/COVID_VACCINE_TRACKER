import logging
from flask import request, g
from flask.views import MethodView
from flask_smorest import Blueprint

from utils.decorators import access_pass
from schemas.user import AddUserSchema
from controllers.user.add_user_controller import AddUserController
from controllers.user.show_users_controller import ShowUserController


blp = Blueprint("Users", __name__, description="User related Operations")

logger = logging.getLogger(__name__)


@blp.route("/users")
class User(MethodView):

    def __init__(self) -> None:
        self.add_user = AddUserController()
        self.get_user = ShowUserController()


    @access_pass(["Admin"])
    @blp.arguments(AddUserSchema)
    def post(self, user_info):
        """Adds new employee into the database"""

        logger.info("{g.request_id}] hits /users post method endpoint")
        return self.add_user.add_user(user_info)


    @access_pass(["Admin"])
    def get(self):
        args = request.args
        dose_date = args.get('dose-date')
        dose_num = args.get('dose-num')
        vaccine_name = args.get('vaccine')

        users = self.get_user.show_all_users(dose_date, dose_num, vaccine_name)
        logger.info("[{g.request_id}] hits /users get method endpoint")
        return users
