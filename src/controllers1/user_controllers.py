from datetime import date

from config.queries.db_queries import DbConfig
from database.database_operations import db
from utils.exceptions import UsernameAlreadyExistsError, NoDataError
from handlers.user_handler import UserHandler


class UserControllers:
    '''
    This class contains methods to perform operations on users.
    '''
    def __init__(self) -> None:
        self.user_handler = UserHandler()


    def add_user(self, add_user_info: str):
        """ This method is used to add a new employee into the database. """
        try:
            self.user_handler.add_user(add_user_info["email"], add_user_info["password"])
            return {
                "message": "User created successfully!"
            }, 201
        except UsernameAlreadyExistsError:
            return {
                "message": "User with this email already exists!!!"
            }, 409
        


    def update_name(self, name, user_id) -> None:
        """ This method is used to update the name of an employee. """
        
        self.user_handler.update_name(name, user_id)

        return {
            "message": "Name updated successfully!"
        }, 200
        


    def update_gender(self, gender, user_id) -> None:
        """ This method is used to update the gender of an employee. """
        
        self.user_handler.update_gender(gender, user_id)

        return {
            "message": "Gender updated successfully!"
        }, 200


    def show_all_users(self) -> list:
        """ This method is used to display the list of all the users. """
        try:
            data = self.user_handler.show_all_users()
            return {
                "UsersList": data
            }, 200
        except NoDataError:
            return {
                "message": "Current no user data available"
            }, 204


    def show_users_by_dose(self, status) -> list:
        """ This method is used to display the list of users based on vaccination status. """
        try:
            if status == 0:
                data = self.user_handler.get_unvaccinated()
            elif status == 1:
                data = self.user_handler.get_dose_1_vaccinated()
            elif status == 2:
                data = self.user_handler.get_dose_2_vaccinated()

            return {
                "UsersList": data
            }, 200
        
        except NoDataError:
            return {
                "message": "Current no user data available"
            }, 204


    def show_users_by_date(self, date: date, dose_num: int) -> list:
        """ This method is used to display list of users who are vaccinated on a particular dose date."""
        try:
            if dose_num == 1:
                query = DbConfig.FETCH_BY_DOSE1_DATE
            else:
                query = DbConfig.FETCH_BY_DOSE2_DATE

            data = db.fetch_data(query, (date,))
           
            return {
                "UsersList": data
            }, 200
    
        except NoDataError:
            return {
                "message": "Current no user data available"
            }, 204


    def show_users_by_vaccine(self, vaccine_name: str) -> list:
        """ This method is used to display list of users who are vaccinated with a particular vaccine. """
        try:
            data = self.user_handler.get_users_by_vaccine(vaccine_name)
            
            return {
                "UsersList": data
            }, 200
        
        except NoDataError:
            return {
                "message": "Current no user data available"
            }, 204