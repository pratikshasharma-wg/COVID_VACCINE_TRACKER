import logging
from flask import g
from flask_jwt_extended import get_jwt_identity

from utils.exceptions import CustomException
from handlers.dose_handlers import DoseHandlers


logger = logging.getLogger(__name__)


class AddDoseController:
    '''
        This class contains method to add dose details.
    '''
    
    def __init__(self) -> None:
        self.dose_handler = DoseHandlers()


    def add_dose_info(self, dose_info) :
        """ This method is used to add dose details by an employee. """

        user_id = get_jwt_identity()
        try:
            self.dose_handler.add_dose(
                user_id, 
                dose_info["vaccine_name"], 
                dose_info["dose_date"], 
                dose_info["dose_cid"],
                1
            )
            logger.info(f"[{g.request_id}] added dose details")

        except CustomException as e:
            return e.dump(), e.code
        return {
                "message": "Dose details addedd successfully!"
            }, 201
