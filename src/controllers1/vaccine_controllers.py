from flask_smorest import abort

from utils.common_helpers import display_table
from handlers.vaccine_handler import VaccineHandler
from database.database_operations import db
from config.queries.db_queries import DbConfig
from utils.exceptions import CustomException


class VaccineControllers:
    '''
    This class contains methods to perform operations related to vaccines.
    '''
    def __init__(self) -> None:
        self.vaccine_handler = VaccineHandler()


    def create_vaccine(self, vaccine_info) -> bool:
        """ This method is used to add new vaccine"""
        try:
            return_val = self.is_vaccine_present(vaccine_info["vaccine_name"])

            if return_val:
                return {
                    "message": f"Vaccine with name: {vaccine_info['vaccine_name']} already exists!"
                }, 409
            
            self.vaccine_handler.create_vaccine(vaccine_info["vaccine_name"])
            return {
                "message": f"Vaccine with name: {vaccine_info['vaccine_name']} Created Successfully!!!"
            }, 201
        
        except CustomException as e:
            return e.dump(), e.code


    def show_vaccines(self) :
        try:
            data = self.vaccine_handler.show_vaccines()
            return {
                "vaccines": [
                    data
                ]
            }, 200
        except CustomException as e:
            return abort(e.code, message=e.message)



    def is_vaccine_present(self, vaccine_id: int) -> bool:
        
        data = self.vaccine_handler.is_vaccine_present(vaccine_id)
        if data:
            return data[0][1]
        else:
            return False
