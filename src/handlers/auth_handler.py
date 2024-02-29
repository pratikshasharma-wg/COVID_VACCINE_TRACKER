import hashlib
from uuid import uuid4

from database.database_operations import db
from config.queries.db_queries import DbConfig
from utils.exceptions import InvalidCredentialsError


BLOCKLIST = set()


class AuthHandler:

    def fetch_user_data(self, email, password):
        
        user_data = db.fetch_data(
            DbConfig.FETCH_AUTH_DATA,
            (email,)
        )

        if not user_data:
            raise InvalidCredentialsError(401,"Unauthorized","Please Enter valid Credentials!!!")
        else:
            user_data = user_data[0]
            db_password = user_data['password']
            password = hashlib.sha256(password.encode()).hexdigest()
            if password != db_password:
                raise InvalidCredentialsError(401,"Unauthorized","Please Enter valid Credentials!!!")
    
        return user_data

    def logout_user(self, rev_token_jti, rev_token_exp):
        """Add jwt to the revoked tokens table"""

        rev_token_id = uuid4()
        db.save_data(
            DbConfig.ADD_REV_TOKEN,
            (rev_token_id, 
            rev_token_jti, 
            rev_token_exp)
        )

    def check_token_in_db(self, jti):
        """Check jwt jti in db"""

        token_present = db.fetch_data(
            DbConfig.FETCH_REV_TOKEN,
            (jti,)
        )
        print(token_present)
        print(db.fetch_data('SELECT * FROM revoked_tokens'))

        return token_present != ()