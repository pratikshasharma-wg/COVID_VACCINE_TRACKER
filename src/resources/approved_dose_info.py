from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from utils.decorators import role_required
from controllers.approve_dose_info.approve_dose_controller import ApproveDoseController
from controllers.approve_dose_info.get_approved_info_controller import GetApprovedInfoController


blp = Blueprint("approve_dose", __name__, description="User related Operations")


@blp.route("/users/approve/{approval_id}")
class ApprovedDoseInfo(MethodView):

    def __init__(self) -> None:
        self.approve_dose = ApproveDoseController
        self.get_approved_info = GetApprovedInfoController()

    
    @role_required(["Admin"])
    def put(self, approval_id):

        return self.approve_dose.approve_info(approval_id)
    
    @role_required(["Admin"])
    def get(self, dose_num, approval_id = None):

        return self.get_approved_info.show_info_to_approve(dose_num)