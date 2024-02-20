import logging
from flask import g
from flask_smorest import abort

from handlers.vaccine_handler import VaccineHandler
from utils.exceptions import CustomException


logger = logging.getLogger(__name__)


class GetVaccineController:
    '''
    This class contains methods to get vaccines.
    '''

    def __init__(self) -> None:
        self.vaccine_handler = VaccineHandler()


    def get_vaccines(self) :
        try:
            logger.info(f"[{g.request_id}] fetched the list of vaccines")
            data = self.vaccine_handler.get_vaccines()
            return {
                "vaccines": data
            }, 200
        
        except CustomException as e:
            return e.dump(), e.code
