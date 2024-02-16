from handlers.user_handler import UserHandler
from utils.exceptions import CustomException


class AddUserController:
    '''
    This class contains methods to add users.
    '''

    def __init__(self) -> None:
        self.user_handler = UserHandler()


    def add_user(self, add_user_info: str):
        """ This method is used to add a new employee into the database. """

        try:
            self.user_handler.add_user(add_user_info["email"], add_user_info["password"])
        except CustomException as e:
            return e.dump(), e.code
        return {
                "message": "User created successfully!"
            }, 201
