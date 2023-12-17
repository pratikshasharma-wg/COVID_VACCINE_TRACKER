import yaml

FPATH = "src\\config\\logs\\logs.yml"

class Logs:

    WELCOME = None
    LOGIN_ATTEMPTS_EXCEEDED = None
    SUCCESS_LOGIN = None
    ADMIN_MSG = None
    EMPLOYEE_MSG = None

    @classmethod
    def load(cls):
        with open(FPATH, 'r') as f:
            data=yaml.safe_load(f)
            cls.WELCOME = data['WELCOME']
            cls.LOGIN_ATTEMPTS_EXCEEDED = data['LOGIN_ATTEMPTS_EXCEEDED']
            cls.SUCCESS_LOGIN = data['SUCCESS_LOGIN']
            cls.ADMIN_MSG = data['ADMIN_MSG']
            cls.EMPLOYEE_MSG = data['EMPLOYEE_MSG']
            