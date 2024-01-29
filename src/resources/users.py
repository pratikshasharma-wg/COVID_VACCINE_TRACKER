from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from utils.decorators import role_required
from schemas.user import AddUserSchema, UpdatePersonalDetailsSchema
from controllers.user.add_user_controller import AddUserController
from controllers.user.show_users_controller import ShowUserController
from controllers.user.update_profile_controller import UpdateProfileController


blp = Blueprint("Users", __name__, description="User related Operations")


@blp.route("/users")
class User(MethodView):

    def __init__(self) -> None:
        self.add_user = AddUserController()
        self.update_profile = UpdateProfileController()
        self.get_user = ShowUserController()


    @role_required(["Admin"])
    @blp.arguments(AddUserSchema)
    def post(self, user_info):

        return self.add_user.add_user(user_info)
    

    @role_required(["Admin"])
    def get(self):
        
        return self.get_user.show_all_users()


    @role_required(["Employee"])
    @blp.arguments(UpdatePersonalDetailsSchema)
    def put(self, user_profile_info):

        return self.update_profile.update_profile(user_profile_info)
