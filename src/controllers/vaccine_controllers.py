from utils.common_helpers import display_table
from database.database_operations import db
from config.queries.db_queries import DbConfig


class VaccineControllers:
    '''
    This class contains methods to perform operations related to vaccines.
    '''

    def create_vaccine(self, vaccine_name) -> bool:
        """ This method is used to add new vaccine"""
        data = db.fetch_data(DbConfig.FETCH_VACCINE_DETAILS, (vaccine_name,))
        if data:
            return False
        else:
            db.save_data(DbConfig.ADD_VACCINE, (vaccine_name,))
            return True

    @staticmethod
    def show_vaccines() -> bool:
        data = db.fetch_data(DbConfig.FETCH_VACCINE)
        return data

    def is_vaccine_present(self, vaccine_id: int) -> bool:
        data = db.fetch_data(
            "SELECT * FROM vaccine WHERE vaccine_id = ?", (vaccine_id,)
        )
        if data:
            return data[0][1]
        else:
            return False
