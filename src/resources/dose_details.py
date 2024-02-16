from flask.views import MethodView
from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required
from utils.decorators import role_required
from controllers.dose.add_dose_controller import AddDoseController
from controllers.dose.update_dose_controller import UpdateDoseController
from schemas.dose_details import AddDoseDetailsSchema, UpdateDoseDetailsSchema


blp = Blueprint("dose details", __name__, description="User dose details related operations")


@blp.route("/users/dose")
class DoseDetails(MethodView):

    def __init__(self) -> None:
        self.add_dose = AddDoseController()
        self.update_dose = UpdateDoseController()


    @role_required(["Employee"])
    @jwt_required()
    @blp.arguments(AddDoseDetailsSchema)
    def post(self, dose_info):
        return self.add_dose.add_dose_info(dose_info)
    

    @role_required(["Employee"])
    @jwt_required()
    @blp.arguments(UpdateDoseDetailsSchema)
    def put(self, update_dose_info):
        return self.update_dose.update_dose_info(update_dose_info)

