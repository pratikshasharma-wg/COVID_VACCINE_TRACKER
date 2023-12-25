import yaml

FPATH = "src\\config\\logs\\logs.yml"


class Logs:
    WELCOME = None
    LOGIN_ATTEMPTS_EXCEEDED = None
    SUCCESS_LOGIN = None
    ADMIN_MSG = None
    EMPLOYEE_MSG = None
    CONNECTION_CLOSED_EXIT_APP = None
    ERROR_OCCURRED = None
    VACCINE_ADDED_SUCCESSFULLY = None
    PROFILE_UPDATED = None
    NEW_USER_ADDED = None
    FIRST_TIME_LOGIN = None

    @classmethod
    def load(cls):
        with open(FPATH, "r") as f:
            data = yaml.safe_load(f)
            
            cls.WELCOME = data["WELCOME"]
            cls.LOGIN_ATTEMPTS_EXCEEDED = data["LOGIN_ATTEMPTS_EXCEEDED"]
            cls.SUCCESS_LOGIN = data["SUCCESS_LOGIN"]
            cls.ADMIN_MSG = data["ADMIN_MSG"]
            cls.EMPLOYEE_MSG = data["EMPLOYEE_MSG"]
            cls.CONNECTION_CLOSED_EXIT_APP = data["CONNECTION_CLOSED_EXIT_APP"]
            cls.ERROR_OCCURRED = data["ERROR_OCCURRED"]
            cls.VACCINE_ADDED_SUCCESSFULLY = data["VACCINE_ADDED_SUCCESSFULLY"]
            cls.PROFILE_UPDATED = data["PROFILE_UPDATED"]
            cls.NEW_USER_ADDED = data["NEW_USER_ADDED"]
            cls.FIRST_TIME_LOGIN = data['FIRST_TIME_LOGIN']