import logging
from flask import g
from flask_jwt_extended import create_access_token

from utils.exceptions import CustomException
from handlers.auth_handler import AuthHandler
from handlers.user_handler import UserHandler


logger = logging.getLogger("auth_controller")


class LoginController:

    def __init__(self) -> None:
        self.auth = AuthHandler()
        self.user = UserHandler()

    def login_user(self, user_info: str) -> None | tuple:
        """
        Method for validating user by their credentials.
        """

        try:

            user_data = self.auth.fetch_user_data(
                user_info["email"], user_info["password"]
            )

            extra_additional_claim = {}

            if user_data["role"] == "Employee":
                user_profile_info = self.user.get_profile(user_data["user_id"])

                extra_additional_claim["profile_updated"] = all(
                    user_profile_info.values()
                )

            access_token = create_access_token(
                identity=user_data["user_id"],
                additional_claims={
                    "role": user_data["role"],
                    "default_pwd_changed": False if user_data["is_def_pwd_changed"] == "False" else True,
                    **extra_additional_claim
                },
            )
            logger.info(f"[{g.request_id}] logged in successfully")

            return {
                "message": "Logged In Successfully!",
                "access_token": access_token,
            }, 200

        except CustomException as e:
            return e.dump(), e.code
