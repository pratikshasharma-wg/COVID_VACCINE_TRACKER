from database.database_operations import db
from config.queries.db_queries import DbConfig
from utils.exceptions import AlreadyExistsError, NoDataError


class VaccineHandler:

    def create_vaccine(self, vaccine_name):
            
        data = db.fetch_data(DbConfig.FETCH_VACCINE_DETAILS, (vaccine_name,))

        if data:
            raise AlreadyExistsError(409, "Conflict", "Vaccine Already exists!!!")
        else:
            db.save_data(DbConfig.ADD_VACCINE, (vaccine_name,))


    def get_vaccines(self):
        
        data = db.fetch_data(DbConfig.FETCH_VACCINE)
        
        return data
        

    def is_vaccine_present(self, vaccine_id):
        
        data = db.fetch_data(
            DbConfig.FETCH_SPECIFIC_VACCINE, (vaccine_id,)
        )
        return data