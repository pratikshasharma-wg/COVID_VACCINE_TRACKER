import logging
from flask import g
from flask.views import MethodView
from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required

from controllers.dose.get_dose_controller import GetDoseController
from utils.decorators import access_pass
from controllers.dose.add_dose_controller import AddDoseController
from controllers.dose.update_dose_controller import UpdateDoseController
from schemas.dose_details import AddDoseDetailsSchema


blp = Blueprint("dose details", __name__, description="User dose details related operations")

logger = logging.getLogger(__name__)


@blp.route("/users/doses")
class DoseDetails(MethodView):

    def __init__(self) -> None:
        self.get_dose = GetDoseController()
        self.add_dose = AddDoseController()
        self.update_dose = UpdateDoseController()

    @access_pass(["Employee"])
    def get(self):
        """Get dose details of a user"""

        logger.info("[{g.request_id}] hits /users/dose post method endpoint")
        return self.get_dose.get_doses()

    @access_pass(["Employee"])
    @blp.arguments(AddDoseDetailsSchema)
    def post(self, dose_info):
        """Adds dose details of a user"""

        logger.info("[{g.request_id}] hits /users/dose post method endpoint")
        return self.add_dose.add_dose_info(dose_info)
    
    @access_pass(["Employee"])
    @blp.arguments(AddDoseDetailsSchema)
    def put(self, update_dose_info):
        """Updates the dose details of a user"""

        logger.info("[{g.request_id}] hits /users/dose put method endpoint")
        return self.update_dose.update_dose_info(update_dose_info)
