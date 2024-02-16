class UsernameAlreadyExistsError(Exception):
    def __init__(self, msg) -> None:
        self.msg = msg

class DoseInfoNotFoundError(Exception):
    def __init__(self) -> None:
        pass

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
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class AlreadyExistsError(CustomException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class NoDataError(CustomException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)