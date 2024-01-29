import hashlib

from database.database_operations import db
from config.queries.db_queries import DbConfig
from utils.exceptions import InvalidCredentialsError


class AuthHandler:

    def fetch_user_data(self, email, password):
        
        user_data = db.fetch_data(
            DbConfig.FETCH_AUTH_DATA,
            (email,)
        )[0]

        db_password = user_data["password"]

        if user_data:
            password = hashlib.sha256(password.encode()).hexdigest()
            
            if password == db_password:
                return user_data  
        
        raise InvalidCredentialsError(401, status = "Unauthorized", message="Please Enter valid Credentials!!!")
              

    # def update_default_password(self, email: str, hashed_password: str):

    #     db.save_data(
    #         DbConfig.UPDATE_PWD,
    #         (
    #             hashed_password,
    #             email,
    #         ),
    #     )