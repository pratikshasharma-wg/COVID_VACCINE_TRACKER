from flask_jwt_extended import get_jwt_identity
from handlers.dose_handlers import DoseHandlers


class UpdateDoseController:
    '''
        This class contains methods to update dose details.
    '''
    
    def __init__(self) -> None:
        self.user_id = get_jwt_identity()
        self.dose_handler = DoseHandlers()


    def update_dose_info(self, update_dose_info) -> None:
        """ This method is used to update the dose 2 details by an employee if already vaccinated with dose 1. """

        try:
            self.dose_handler.update_dose_info(
                self.user_id,  
                update_dose_info["dose_date"], 
                update_dose_info["dose_cid"]
            )

            return {
                "message": "Dose details updated successfully!"
            }
        
        except Exception:
            ...

    