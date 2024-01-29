from flask_jwt_extended import get_jwt_identity

from handlers.dose_handlers import DoseHandlers


class AddDoseController:
    '''
        This class contains method to add dose details.
    '''
    
    def __init__(self) -> None:
        self.dose_handler = DoseHandlers()


    def add_dose_info(self, dose_info: str) :
        """ This method is used to add dose details by an employee. """

        self.user_id = get_jwt_identity()

        self.dose_handler.add_dose_info(
            self.user_id, 
            dose_info["vaccine_name"], 
            dose_info["dose_1_date"], 
            dose_info["dose_1_cid"]
        )

        return {
            "message": "Dose details addedd successfully!"
        }, 201