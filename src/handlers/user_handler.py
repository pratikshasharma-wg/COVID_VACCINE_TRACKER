import shortuuid

from config.queries.db_queries import DbConfig
from database.database_operations import db
from utils.exceptions import AlreadyExistsError, NoDataError

class UserHandler:

    def add_user(self, email, password):

        user_id = user_id = int(shortuuid.ShortUUID("123456789").random(4))

        if db.fetch_data(DbConfig.FETCH_AUTH_DATA, (email.lower(),)):
            raise AlreadyExistsError(409, "Conflict", "User with this email already exists!!!")

        db.save_data(
        DbConfig.ADD_USER,
        (
            user_id,
            email,
            password,
        ),
        )

        db.save_data(
            DbConfig.ADD_USER_DETAILS,
            (
                user_id,
                email,
            ),
        )
        

    def get_all_users(self):
     
        data = db.fetch_data(DbConfig.FETCH_USER_DETAILS)

        if data is None:
            raise NoDataError(204, "No content", "Currently no user data available!!!")
        
        return data

            
    def update_profile(self, name, gender, user_id):
        
        db.save_data(DbConfig.UPDATE_NAME, (name, user_id))
        db.save_data(DbConfig.UPDATE_GENDER, (gender, user_id))

    
    def get_unvaccinated(self):
        
        data = db.fetch_data(
            DbConfig.FETCH_DOSE_0_EMPLOYEES
        )
        if data is None:
            raise NoDataError(204, "No content", "Currently no user data available!!!")
        
        return data
    

    def get_dose_1_vaccinated(self):
        
        data = db.fetch_data(
            DbConfig.FETCH_DOSE_1_EMPLOYEES
        )
        if data is None:
            raise NoDataError(204, "No content", "Currently no user data available!!!")
        
        return data


    def get_dose_2_vaccinated(self):
        
        data = db.fetch_data(
                DbConfig.FETCH_DOSE_2_EMPLOYEES
        )
        if data is None:
            raise NoDataError(204, "No content", "Currently no user data available!!!")
        
        return data
    

    def get_users_by_vaccine(self, vaccine_name):
        
        data = db.fetch_data(
            DbConfig.FETCH_BY_VACCINE,
            (vaccine_name,)
        )
        if data is None:
            raise NoDataError(204, "No content", "Currently no user data available!!!")
        
        return data
    