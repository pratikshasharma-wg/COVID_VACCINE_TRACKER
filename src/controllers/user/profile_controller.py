from flask import g
from flask_jwt_extended import get_jwt_identity

from utils.exceptions import CustomException
from handlers.user_handler import UserHandler


class ProfileController:
    '''
    This class contains methods to update profile of user.
    '''

    def __init__(self) -> None:
        self.user_handler = UserHandler()


    def update_profile(self, user_profile_info):
        """ This method is used to update the profile of the user. """
        user_id = get_jwt_identity()
        self.user_handler.update_profile(
            user_profile_info["name"],
            user_profile_info["gender"],
            user_id
        )

        return {
            "message": "Profile updated successfully!!!"
        }, 200
    

    def show_profile(self):
        """ This method is used to see the profile info. """
        user_id = get_jwt_identity()
        profile_data = self.user_handler.get_profile(user_id)
        return {
            "details": profile_data
        }, 200