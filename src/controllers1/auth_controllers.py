"""
    Module for validating user, changing their default passsword, and providing them role based access
"""
import logging
from flask import abort
from datetime import timedelta
from flask_jwt_extended import create_access_token

from utils.exceptions import InvalidCredentialsError
from handlers.auth_handler import AuthHandler


logger = logging.getLogger("auth_controller")


class AuthControllers:

    """
    This class contains methods for validating user, providing role based access and changing their default password.
    """
    def __init__(self) -> None:
        self.auth_bl = AuthHandler()


    def validate_user(self, user_info: str) -> None|tuple:
        """
        Method for validating user by their credentials
        """
        try:

            user_data = self.auth_bl.fetch_user_data(
                user_info["email"], 
                user_info["input_password"]
            )

            access_token = create_access_token(
                identity = user_data["user_id"],
                expires_delta = timedelta(minutes=20),
                additional_claims = {"role": user_data["role"]}
            )

            return {
                "message": "Logged In Successfully!",
                "access_token": access_token
            }, 200
                
        except InvalidCredentialsError :
            abort(401, message="Please Enter valid Credentials!!!")


    # def update_default_password(self, email: str, hashed_password: str) -> bool:

    #     try:
    #         user_data = self.auth_bl.update_default_password(email, hashed_password)
            
    #         if user_data:
    #             return {
    #                 "message" : "password updated successfully!"
    #             }
    #     except DbError:
    #         abort(500, message = "Something went wrong")