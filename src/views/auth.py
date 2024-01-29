import logging
import time
import hashlib
import maskpass
from os import system

from views.admin import AdminViews
from config.prints.prints import Prints
from views.employee import EmployeeViews
from config.prompts.prompts import PromptsConfig
from controllers.auth_controllers import AuthControllers
from utils.input_validators import input_valid_password


logger = logging.getLogger("auth_view")


class AuthViews:
    """
    Class that authenticates the user and provides role based access to the authenticated user
    """

    def __init__(self) -> None:
        self.auth_controller_obj = AuthControllers()
        self.__login_attempts = 3


    def start(self) -> None:
        """Method that displays the login menu"""

        while True:
            choice = input(PromptsConfig.LOGIN_PROMPT)
            if choice == "1":
                system("cls")
                print(Prints.WELCOME_TO_LOGIN)
                self.login()
            elif choice == "2":
                return
            else:
                print(Prints.ENTER_VALID)


    def login(self) -> None:
        """
        Method that takes user credentials as input and validates the user
        Parameter : self
        Return type : None
        """
        while self.__login_attempts:
            self.username = input(PromptsConfig.ENTER_USERNAME)
            self.password = maskpass.askpass(PromptsConfig.ENTER_PWD)
            self.hashed_password = hashlib.sha256(self.password.encode()).hexdigest()

            user_info = self.auth_controller_obj.validate_user(
                self.username, self.password
            )

            if user_info:
                break

            print(Prints.INVALID_CREDENTIALS)
            self.__login_attempts -= 1
            print(Prints.ATTEMPTS_LEFT.format(attempts=self.__login_attempts))
            continue

        if self.__login_attempts == 0:
            time.sleep(3)
            system("cls")
            self.start()
        else:
            self.role_of_user(user_info)
            return

    def change_default_pwd(self, email: str, new_password: str, confirm_password: str) -> bool:
        """
        This method is used to change default password on first time login.
        """

        while True:
            new_password = input_valid_password(PromptsConfig.NEW_PWD)
            confirm_password = input_valid_password(PromptsConfig.CONFIRM_NEW_PWD)

            if new_password != confirm_password:
                print(Prints.CONFIRM_PWD_NOT_MATCHED)
                continue
            else:
                hashed_password = hashlib.sha256(new_password.encode()).hexdigest()
                break

        logger.info("Default Password changed for employee username : ".format(email))
        return True

    def role_of_user(self, user_info: tuple) -> bool:
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