from utils.exceptions import CustomException
from handlers.user_handler import UserHandler


class ShowUserController:
    '''
    This class contains methods to get all users.
    '''

    def __init__(self) -> None:
        self.user_handler = UserHandler()


    def show_all_users(self) -> list:
        """ This method is used to display the list of all the users. """

        try:
            data = self.user_handler.get_all_users()

            return {
                "UsersList": data
            }, 200
        
        except CustomException as e:
            return e.dump(), e.code