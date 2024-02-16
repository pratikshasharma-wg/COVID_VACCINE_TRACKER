from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from utils.decorators import role_required
from controllers.user.show_users_controller import ShowUserController


blp = Blueprint("FilterUsers", __name__, description="User Display related Operations")


@blp.route("/users/filter-by-dose")
class FilterByDose(MethodView):

    def __init__(self) -> None:
        self.get_user = ShowUserController()

    @role_required(["Admin"])
    def get(self, dose_num):

        return self.get_user.show_users_by_dose(dose_num)
        # query_parameter = request.args

        # if "dose_num" in query_parameter:
        #     users = filter(lambda user: users[4] == request.args["dose_num"], users)
        # if "date" in query_parameter:
        #     users = filter(lambda _: users[])
        # return {
        #     "users": users
        # }

@blp.route("/users/filter-by-date")
class FilterByDate(MethodView):

    def __init__(self) -> None:
        self.get_user = ShowUserController()
    
    @role_required
    def get(self, date):

        return self.get_user.show_users_by_date(date)
    
@blp.route("/users/filter-by-vaccine")
class FilterByVaccine(MethodView):

    def __init__(self) -> None:
        self.get_user = ShowUserController()

    @role_required
    def get(self, vaccine_name):

        return self.get_user.show_users_by_vaccine(vaccine_name)