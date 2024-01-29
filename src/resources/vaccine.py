from flask.views import MethodView
from flask_smorest import Blueprint
from schemas.vaccine import CreateVaccineSchema
from utils.decorators import role_required
from controllers.vaccine.add_vaccine_controller import AddVaccineController
from controllers.vaccine.get_vaccines_controller import GetVaccineController


blp = Blueprint("Vaccine", __name__, description="Operations on Vaccines")


@blp.route("/vaccine")
class Vaccine(MethodView):

    def __init__(self) -> None:
        self.add_vaccine = AddVaccineController()
        self.get_vaccine = GetVaccineController()


    @role_required(["Admin"])
    @blp.arguments(CreateVaccineSchema)
    def post(self, vaccine_info):

        return self.add_vaccine.create_vaccine(vaccine_info)
    

    @role_required(["Admin", "Employee"])
    def get(self):

        return self.get_vaccine.get_vaccines()