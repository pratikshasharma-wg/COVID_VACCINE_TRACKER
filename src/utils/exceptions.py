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