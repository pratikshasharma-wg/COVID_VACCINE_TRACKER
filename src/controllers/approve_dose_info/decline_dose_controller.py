import logging
from flask import g

from utils.exceptions import CustomException
from handlers.approve_dose_handler import ApproveDoseHandler


logger = logging.getLogger(__name__)


class DeclineDoseController:
        
    def __init__(self) -> None:
        self.decline_dose_handler = ApproveDoseHandler()
            

    def _info(self, approval_id: int) -> None:
        """ 
            This method is used to approve the details by admin. 
        """
        try:
            self.approve_dose_handler.decline_info(approval_id)
            logger.info(f"[{g.request_id}] approved user details")

            return {
                "message": "User approval declined!"
            }, 200

        except CustomException as e:
            return e.dump(), e.code
