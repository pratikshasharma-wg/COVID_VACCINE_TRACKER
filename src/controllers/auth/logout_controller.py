from flask_jwt_extended import get_jwt

from handlers.auth_handler import AuthHandler


class LogoutController:

    def logout_user(self):
        claims = get_jwt()
        jwt_jti = claims["jti"]
        exp = claims["exp"]
        AuthHandler().logout_user(jwt_jti, exp)
        return {
            "message": "You are logged out!"
        }, 200
