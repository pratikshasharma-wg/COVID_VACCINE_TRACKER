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

        if data is None:
            raise NoDataError(204, "No Content", "Currently no data available!!!")
        
        return data
        

    # def is_vaccine_present(self, vaccine_id):
    #     try:
    #         data = db.fetch_data(
    #             "SELECT * FROM vaccine WHERE vaccine_id = ?", (vaccine_id,)
    #         )
    #         return data
    #     except Exception:
    #         ...