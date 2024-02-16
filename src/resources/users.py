from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint
from utils.decorators import role_required
from schemas.user import AddUserSchema
from controllers.user.add_user_controller import AddUserController
from controllers.user.show_users_controller import ShowUserController
from utils.exceptions import NoDataError


blp = Blueprint("users", __name__, description="User related Operations")


@blp.route("/users")
class User(MethodView):

    def __init__(self) -> None:
        self.add_user = AddUserController()
        self.get_user = ShowUserController()


    @role_required(["Admin"])
    @blp.arguments(AddUserSchema)
    def post(self, user_info):

        return self.add_user.add_user(user_info)
    

    @role_required(["Admin"])
    def get(self):
        args = request.args
        dose_date = args.get('dose-date')
        dose_num = args.get('dose-num')
        vaccine_name = args.get('vaccine')

        if args is None or dose_date or dose_num or vaccine_name:
            users = self.get_user.show_all_users(dose_date, dose_num, vaccine_name)
            return users
        return {"code":404, "status":"No content", "message":"Currently no user data available!!!"}