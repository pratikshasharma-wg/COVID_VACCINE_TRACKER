from flask_smorest import abort

from handlers.vaccine_handler import VaccineHandler
from utils.exceptions import CustomException


class GetVaccineController:
    '''
    This class contains methods to get vaccines.
    '''

    def __init__(self) -> None:
        self.vaccine_handler = VaccineHandler()


    def get_vaccines(self) :
        try:
            data = self.vaccine_handler.get_vaccines()
            return {
                "vaccines": data
            }, 200
        
        except CustomException as e:
            return abort(e.code, message=e.message)
