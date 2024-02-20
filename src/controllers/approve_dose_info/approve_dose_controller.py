from flask import g

from utils.exceptions import CustomException
from handlers.approve_dose_handler import ApproveDoseHandler

class ApproveDoseController:
        
    def __init__(self) -> None:
        self.approve_dose_handler = ApproveDoseHandler()
            

    def approve_info(self, approval_id: int) -> None:
        """ 
            This method is used to approve the details by admin. 
        """
        try:

            self.approve_dose_handler.approve_info(approval_id)

            return {
                "message": "User details approved successfully!"
            }, 200

        except CustomException as e:
            return e.dump(), e.code
