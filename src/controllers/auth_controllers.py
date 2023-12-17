"""
    Module for validating user, changing their default passsword, and providing them role based access
"""
import hashlib
import logging

from database.database_operations import db
from config.prompts.prompts import PromptsConfig
from config.logs.logs import Logs
from config.prints.prints import Prints
from config.queries.db_queries import DbConfig
from views.employee import EmployeeViews
from utils.input_validators import input_valid_password

logger = logging.getLogger('auth_controller')

class AuthControllers:

    """
        Class containing methods for validating user, providing role based access and changing their default password.
        ...
        Attributes
        ----------
        obj_db_helper -> object of DatabaseHelper class for accessing its methods.

        Methods
        -------
        first_login() -> private method, for checking if password entered matches with default password.
        role_based_access() -> private method, for providing role based access to the valid user
        validate_user() -> checks if the user entered credentials is a valid password or not 
    """

    def __init__(self) -> None:
        pass

    def validate_user(self, email : str, input_password : str) -> bool:
        """
            Method for validating user by their credentials
            Paramters : self, username, input_password
            Return type : bool
        """
        user_data = db.fetch_data(DbConfig.FETCH_AUTH_DATA, (email,))

        if user_data:
            user_id = user_data[0][0]
            email = user_data[0][1]
            password = user_data[0][2]
            role = user_data[0][3]
            is_def_pwd_changed = user_data[0][4]
            
            hashed_password = hashlib.sha256(input_password.encode()).hexdigest()

            if hashed_password == password:
                if is_def_pwd_changed == 'False':
                    logger.info("User logged in first time")
                    self.change_default_pwd(email)
                    EmployeeViews(user_id).update_profile()

            return user_data
        return False
    
        
    def change_default_pwd(self, email : str) -> bool:
        """
        Change default password on first time login.
        """
        
        while True:
            new_password = input_valid_password(PromptsConfig.NEW_PWD)
            confirm_password = input_valid_password(PromptsConfig.CONFIRM_NEW_PWD)

            if new_password != confirm_password:
                print(Prints.CONFIRM_PWD_NOT_MATCHED)
                continue
            else:
                hashed_password = hashlib.sha256(new_password.encode()).hexdigest()
                db.save_data(DbConfig.UPDATE_PWD,(hashed_password, email,))
                break    

        logger.info("Default Password changed for employee username : ".format(email))
        return True