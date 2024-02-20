from flask import g

from config.prints.prints import Prints
from handlers.vaccine_handler import VaccineHandler
from utils.exceptions import CustomException


class AddVaccineController:
    '''
    This class contains methods to add vaccines.
    '''

    def __init__(self) -> None:
        self.vaccine_handler = VaccineHandler()


    def create_vaccine(self, vaccine_info) -> bool:
        """ This method is used to add new vaccine"""

        try:
            
            self.vaccine_handler.create_vaccine(vaccine_info["vaccine_name"])
            return {
                Prints.MSG : f"Vaccine with name: {vaccine_info['vaccine_name']} added successfully!!!"
            }, 201
        
        except CustomException as e:
            return e.dump(), e.code