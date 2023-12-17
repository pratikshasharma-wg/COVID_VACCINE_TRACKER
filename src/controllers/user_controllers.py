from typing import Union
from datetime import date

from config.queries.db_queries import DbConfig
from utils.common_helpers import display_table
from database.database_operations import db
from config.prints.prints import Prints

class UserControllers:
    

    def create_user(self, user_id: int, username: str, pwd: hash) -> None:
        db.save_data(
                    DbConfig.ADD_USER,
                    (user_id, username, pwd,)
        )
        
        db.save_data(
                    DbConfig.ADD_USER_DETAILS,
                    (user_id, username,)
        )


    def update_name(self, name, user_id) -> None:
        db.save_data(
                    DbConfig.UPDATE_NAME,
                    (name,user_id)
                    )

    def update_gender(self, gender, user_id) -> None:
        db.save_data(
                    DbConfig.UPDATE_GENDER,
                    (gender,user_id)
                    )
        
    def show_all_users(self) -> list:
        data = db.fetch_data(DbConfig.FETCH_USER_DETAILS)
        return data
        

    def show_users_by_dose(self, status) -> list:
        if status == 0:
            data = db.fetch_data('''SELECT user_details.user_id, user_details.email
                                    FROM user_details
                                    LEFT JOIN dose_details ON user_details.user_id = dose_details.user_id
                                    WHERE dose_details.user_id IS NULL''')   
        elif status == 1:
            data = db.fetch_data('''SELECT u.user_id, u.email, d.vaccine_name FROM user_details as u JOIN dose_details as d ON u.user_id
                                 = d.user_id WHERE d.dose_num = 1
                                 ''')      
        elif status == 2:
            data = db.fetch_data('''SELECT u.user_id, u.email, d.vaccine_name FROM user_details as u JOIN dose_details as d ON u.user_id
                                 = d.user_id WHERE d.dose_num = 2
                                 ''')
        return data
            
        
    def show_users_by_date(self,date: date, dose_num: int) -> list:
        if dose_num == 1 :
            query = DbConfig.FETCH_BY_DOSE1_DATE
        else :
            query = DbConfig.FETCH_BY_DOSE2_DATE
            
        data = db.fetch_data(query, (date,))
        return data
    
    def show_users_by_vaccine(self, vaccine_name : str) -> list:
        data = db.fetch_data(DbConfig.FETCH_BY_VACCINE, (vaccine_name,))
        return data