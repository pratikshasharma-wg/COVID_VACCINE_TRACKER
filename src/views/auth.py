"""
    Module for taking user credentials as input.
    This module contains max login attempts which are reduced by each invalid login.
"""
import logging
import time
import hashlib
import maskpass
from os import system

from config.prints.prints import Prints
from controllers.auth_controllers import AuthControllers
from config.prompts.prompts import PromptsConfig
from views.admin import AdminViews
from views.employee import EmployeeViews

logger = logging.getLogger('auth_view')

class AuthViews:
    '''
        Class that authenticates the user and provides role based access to the authenticated user
        ...
        Attributes
        ----------
        login_attempts -> maximum login attempts for each user, i.e 3

        Methods
        -------
        start() -> it starts the app and displays login menu
        login() -> it takes user credentials as input and validates the user
        role_of_user() -> it provides role based access to the user
    '''
  
    def __init__(self) -> None:
        self.auth_controller_obj = AuthControllers()
        self.__login_attempts = 3


    def start(self) -> None:
        ''' Method that displays the login menu '''

        while True:
            choice = (input(PromptsConfig.LOGIN_PROMPT))
            if choice == '1':
                system('cls')
                print(Prints.WELCOME_TO_LOGIN)
                self.login()
            elif choice == '2':
                return
            else:
                print(Prints.ENTER_VALID)


    def login(self) -> None:
        '''
            Method that takes user credentials as input and validates the user
            Parameter : self
            Return type : None
        '''
        while self.__login_attempts:
            self.username = input(PromptsConfig.ENTER_USERNAME)
            self.password = maskpass.askpass(PromptsConfig.ENTER_PWD)
            self.hashed_password = hashlib.sha256(self.password.encode()).hexdigest()

            user_info = self.auth_controller_obj.validate_user(self.username, self.password)

            if user_info :
                break

            print(Prints.INVALID_CREDENTIALS)
            self.__login_attempts -= 1
            print(Prints.ATTEMPTS_LEFT.format(attempts = self.__login_attempts))
            continue

        if self.__login_attempts == 0:
            time.sleep(3)
            system('cls')
            self.start()
        else:
            self.role_of_user(user_info)
            return 
        

    def role_of_user(self,user_info : tuple) -> bool:
        """
            Method for providig role based access to authenticated user
            Parameters : self, user_info
            Return type : bool
        """
        role = user_info[0][3]
        
        if role == "Admin":
            admin_obj = AdminViews(user_info[0][0])     
            admin_obj.admin_menu()
            return True
        elif role == "Employee":
            employee_obj = EmployeeViews(user_info[0][0])
            employee_obj.emp_menu()
            return True
        else:
            return False