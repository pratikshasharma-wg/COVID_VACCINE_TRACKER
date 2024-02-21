class UsernameAlreadyExistsError(Exception):
    ...


class DoseInfoNotFoundError(Exception):
    ...


class CIDAlreadyExistsError(Exception):
    def __init__(self, msg) -> None:
        self.msg = msg


class EmptyNameError(Exception):
    def __init__(self, msg) -> None:
        self.msg = msg


class VaccineNameError(Exception):
    def __init__(self, msg) -> None:
        self.msg = msg


class ValidNameError(Exception):
    def __init__(self, msg) -> None:
        self.msg = msg


class CustomException(Exception):

    def __init__(self, code, status, message) -> None:
        # code, status, message = args
        self.code = code
        self.status = status
        self.message = message 

    def dump(self):
        return {
            "code": self.code,
            "status": self.status,
            "message": self.message
        }


class InvalidCredentialsError(CustomException):
    ...


class AlreadyExistsError(CustomException):
    ...


class NoDataError(CustomException):
    ...


class FailedValidation(CustomException):
    ...
