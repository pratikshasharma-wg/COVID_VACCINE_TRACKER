import logging
from flask import g
from flask_jwt_extended import get_jwt_identity

from utils.exceptions import CustomException
from handlers.dose_handlers import DoseHandlers


logger = logging.getLogger(__name__)


class GetDoseController:
    '''
        This class contains method to get dose details.
    '''
    
    def __init__(self) -> None:
        self.dose_handler = DoseHandlers()


    def get_doses(self) :
        """ This method is used to get dose details by an employee. """

        user_id = get_jwt_identity()
        try:
            data = self.dose_handler.get_user_doses(user_id)
            logger.info(f"[{g.request_id}] get dose details")
        except CustomException as e:
            return e.dump(), e.code
        return {
                "doses": data
            }, 200
