from flask_jwt_extended import get_jwt_identity

from utils.exceptions import CustomException
from handlers.user_handler import UserHandler


class UpdateProfileController:
    '''
    This class contains methods to update profile of user.
    '''

    def __init__(self) -> None:
        self.user_id = get_jwt_identity()
        self.user_handler = UserHandler()


    def update_profile(self, user_profile_info):
        """ This method is used to update the profile of the user. """

        self.user_handler.update_profile(
            user_profile_info["name"],
            user_profile_info["gender"],
            self.user_id
        )

        return {
            "message": "Profile updated successfully!!!"
        }, 200