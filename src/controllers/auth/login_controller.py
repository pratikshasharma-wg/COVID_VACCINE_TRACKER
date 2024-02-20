import logging
from flask import g
from flask_jwt_extended import create_access_token

from utils.exceptions import CustomException
from handlers.auth_handler import AuthHandler


logger = logging.getLogger("auth_controller")


class LoginController:

    def __init__(self) -> None:
        self.auth = AuthHandler()


    def login_user(self, user_info: str) -> None|tuple:
        """
        Method for validating user by their credentials.
        """

        try:

            user_data = self.auth.fetch_user_data(
                user_info["email"], 
                user_info["password"]
            )

            access_token = create_access_token(
                identity = user_data["user_id"],
                additional_claims = {"role": user_data['role']}    
            )

            return {
                "message": "Logged In Successfully!",
                "access_token": access_token
            }, 200
    
        except CustomException as e:
            return e.dump(), e.code
