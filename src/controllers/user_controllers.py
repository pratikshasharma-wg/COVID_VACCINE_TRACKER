from typing import Union
from datetime import date

from config.queries.db_queries import DbConfig
from utils.common_helpers import display_table
from database.database_operations import db
from config.prints.prints import Prints


class UserControllers:
    '''
    This class contains methods to perform operations on users.
    '''

    def create_user(self, user_id: int, username: str, pwd: hash) -> None:
        """ This method is used to add a new employee into the database. """

        db.save_data(
            DbConfig.ADD_USER,
            (
                user_id,
                username,
                pwd,
            ),
        )

        db.save_data(
            DbConfig.ADD_USER_DETAILS,
            (
                user_id,
                username,
            ),
        )


    def update_name(self, name, user_id) -> None:
        """ This method is used to update the name of an employee. """

        db.save_data(DbConfig.UPDATE_NAME, (name, user_id))


    def update_gender(self, gender, user_id) -> None:
        """ This method is used to update the gender of an employee. """

        db.save_data(DbConfig.UPDATE_GENDER, (gender, user_id))


    def show_all_users(self) -> list:
        """ This method is used to display the list of all the users. """

        data = db.fetch_data(DbConfig.FETCH_USER_DETAILS)
        return data


    def show_users_by_dose(self, status) -> list:
        """ This method is used to display the list of users based on vaccination status. """

        if status == 0:
            data = db.fetch_data(
                DbConfig.FETCH_DOSE_0_EMPLOYEES
            )
        elif status == 1:
            data = db.fetch_data(
                DbConfig.FETCH_DOSE_1_EMPLOYEES
            )
        elif status == 2:
            data = db.fetch_data(
                DbConfig.FETCH_DOSE_2_EMPLOYEES
            )
        return data


    def show_users_by_date(self, date: date, dose_num: int) -> list:
        """ This method is used to display list of users who are vaccinated on a particular dose date."""

        if dose_num == 1:
            query = DbConfig.FETCH_BY_DOSE1_DATE
        else:
            query = DbConfig.FETCH_BY_DOSE2_DATE

        data = db.fetch_data(query, (date,))
        return data


    def show_users_by_vaccine(self, vaccine_name: str) -> list:
        """ This method is used to display list of users who are vaccinated with a particular vaccine. """

        data = db.fetch_data(DbConfig.FETCH_BY_VACCINE, (vaccine_name,))
        return data