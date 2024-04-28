import logging
from flask import g
from flask.views import MethodView
from flask_smorest import Blueprint


from controllers.approve_dose_info.decline_dose_controller import DeclineDoseController
from utils.decorators import access_pass
from controllers.user.show_users_controller import ShowUserController
from controllers.approve_dose_info.approve_dose_controller import ApproveDoseController
from controllers.approve_dose_info.get_approved_info_controller import GetApprovedInfoController


approve_blp = Blueprint("approve dose", __name__, description="Approved dose info related Operations")
get_blp = Blueprint("get approved dose info", __name__, description="Get info to approve")

logger = logging.getLogger(__name__)


@get_blp.route("/users/approve")
class GetInfoToApprove(MethodView):

    def __init__(self) -> None:
        self.get_approved_info = GetApprovedInfoController()
        self.show_users = ShowUserController()
    

    @access_pass(["Admin"])
    def get(self):
        
        logger.info(f"[{g.request_id}] hits /users/approve get method endpoint")
        return self.get_approved_info.show_info_to_approve()


@approve_blp.route("/users/approve/<string:approval_id>")
class ApproveDoseInfo(MethodView):

    def __init__(self) -> None:
        self.approve_dose = ApproveDoseController()
        self.decline_dose = DeclineDoseController()


    @access_pass(["Admin"])
    def put(self, approval_id):
        """Approves the dose details of an employee"""
        
        logger.info(f"[{g.request_id}] hits /users/approve/{approval_id} put method endpoint")
        approval_id = int(approval_id)
        return self.approve_dose.approve_info(approval_id)

    @access_pass(["Admin"])
    def delete(self, approval_id):
        """Decline the dose details of an employee"""
        logger.info(f"[{g.request_id}] hits /users/approve/{approval_id} delete method endpoint")
        return self.decline_dose.decline_info(approval_id)
