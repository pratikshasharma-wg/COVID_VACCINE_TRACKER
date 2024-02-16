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
        
        if user_data:
            db_password = user_data['password']
            password = hashlib.sha256(password.encode()).hexdigest()
            if password != db_password:
                raise InvalidCredentialsError(401,"Unauthorized","Please Enter valid Credentials!!!")
    
        return user_data

              

    # def update_default_password(self, email: str, hashed_password: str):

    #     db.save_data(
    #         DbConfig.UPDATE_PWD,
    #         (
    #             hashed_password,
    #             email,
    #         ),
    #     )