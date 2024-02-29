import logging
from flask import g
from flask.views import MethodView
from flask_smorest import Blueprint

from schemas.vaccine import CreateVaccineSchema
from utils.decorators import access_pass
from controllers.vaccine.add_vaccine_controller import AddVaccineController
from controllers.vaccine.get_vaccines_controller import GetVaccineController


blp = Blueprint("vaccine", __name__, description="Operations on Vaccines")

logger = logging.getLogger(__name__)


@blp.route("/vaccines")
class Vaccine(MethodView):

    def __init__(self) -> None:
        self.add_vaccine = AddVaccineController()
        self.get_vaccine = GetVaccineController()


    @access_pass(["Admin"])
    @blp.arguments(CreateVaccineSchema)
    def post(self, vaccine_info):
        """Adds new vaccine"""

        logger.info(f"[{g.request_id}] hits /vaccines post method endpoint")
        return self.add_vaccine.create_vaccine(vaccine_info)
    

    @access_pass(["Admin", "Employee"])
    def get(self):
        """Retrieves the list of vaccines"""

        logger.info(f"[{g.request_id}] hits /vaccines get method endpoint")
        return self.get_vaccine.get_vaccines()
