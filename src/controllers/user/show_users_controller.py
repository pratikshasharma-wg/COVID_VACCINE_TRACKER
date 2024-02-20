from flask import g
from datetime import date

from config.queries.db_queries import DbConfig
from database. database_operations import db
from utils.exceptions import CustomException
from handlers.user_handler import UserHandler


class ShowUserController:
    '''
    This class contains methods to get all users.
    '''

    def __init__(self) -> None:
        self.user_handler = UserHandler()


    def show_all_users(self, dose_date, dose_num, vaccine_name) -> list:
        """ This method is used to display the list of all the users. """

        try:
            data = self.user_handler.get_all_users(dose_date, dose_num, vaccine_name)

            return {
                "users": data
            }, 200
        
        except CustomException as e:
            return e.dump(), e.code
        
        
    def show_users_by_dose(self, dose_num) -> list:
        """ This method is used to display the list of users based on vaccination status. """
        try:
            if dose_num == 0:
                data = self.user_handler.get_unvaccinated()
            elif dose_num == 1:
                data = self.user_handler.get_dose_1_vaccinated()
            elif dose_num == 2:
                data = self.user_handler.get_dose_2_vaccinated()

            return {
                "users": data
            }, 200
        
        except CustomException as e:
            return e.dump(), e.code
        

    def show_users_by_date(self, date: date) -> list:
        """ This method is used to display list of users who are vaccinated on a particular dose date."""
        try:
            data = self.user_handler.get_users_by_date(date)
            if data:
                return {
                    "users": data
                }, 200
        
        except CustomException as e:
            return e.dump(), e.code
        

    def show_users_by_vaccine(self, vaccine_name) -> list:

        try:
            data = self.user_handler.get_users_by_vaccine(vaccine_name)
            if data:
                return {
                    "users": data
                }, 200
        
        except CustomException as e:
            return e.dump(), e.code

    def show_users_approved_dose(self) -> list:

        try:
            data = self.user_handler.get_approved_dose_users()
            if data:
                return {
                    "users": data
                    }, 200
        
        except CustomException as e:
            return e.dump(), e.code
