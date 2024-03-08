import logging
from flask import g
from flask_jwt_extended import get_jwt_identity

from handlers.auth_handler import AuthHandler


class ChangePasswordController:

    def __init__(self) -> None:
        self.auth = AuthHandler()

    def change_password(self, new_password):
        """Changes the password of the user."""

        user_id = get_jwt_identity()
        self.auth.change_password(user_id, new_password)
        return {
            "message": "Your password changed successfully!"
        }, 200
