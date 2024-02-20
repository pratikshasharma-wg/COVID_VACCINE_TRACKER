import shortuuid
import hashlib

from config.queries.db_queries import DbConfig
from database.database_operations import db
from utils.exceptions import AlreadyExistsError, NoDataError

class UserHandler:

    def add_user(self, email, password):

        user_id = user_id = int(shortuuid.ShortUUID("123456789").random(4))

        if db.fetch_data(DbConfig.FETCH_AUTH_DATA, (email.lower(),)):
            raise AlreadyExistsError(409, "Conflict", "User with this email already exists!!!")

        password = hashlib.sha256(password.encode()).hexdigest()

        db.save_data(
            DbConfig.ADD_USER,(
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
        

    def get_all_users(self, dose_date, dose_num, vaccine_name):
     
        users = db.fetch_data(DbConfig.FETCH_USER_DETAILS)
        if dose_date:
            users = tuple(filter(lambda user: user["dose_date"] == dose_date, users))
        if dose_num:
            users = tuple(filter(lambda user: user["dose_num"] == dose_num, users))
        if vaccine_name:
            users = tuple(filter(lambda user: user["vaccine_name"] == vaccine_name, users))
        
        return users

            
    def update_profile(self, name, gender, user_id):
        
        db.save_data(DbConfig.UPDATE_NAME, (name, user_id))
        db.save_data(DbConfig.UPDATE_GENDER, (gender, user_id))


    def get_profile(self, user_id):
        data = db.fetch_data(DbConfig.FETCH_PROFILE, (user_id,))
        return data[0]

    
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
    
    def get_users_by_date(self, date):

        data = db.fetch_data(DbConfig.FETCH_USERS_BY_DATE, (date,))
        if data is None:
            raise NoDataError(204, "No Content", "Currently no users data available!")

        return data

    def get_approved_dose_users(self):

        data = db.fetch_data(DbConfig.FETCH_APPROVED_DATA)
        if data is None:
            raise NoDataError(204, "No Content", "Currently no users data available!")
        
        return data
