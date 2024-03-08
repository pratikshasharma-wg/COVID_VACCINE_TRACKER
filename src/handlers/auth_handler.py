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
            self.user_data = user_data[0]
            db_password = self.user_data['password']
            password = hashlib.sha256(password.encode()).hexdigest()
            if password != db_password:
                raise InvalidCredentialsError(401,"Unauthorized","Please Enter valid Credentials!!!")
    
        return self.user_data

    def logout_user(self, rev_token_jti, rev_token_exp):
        """Add jwt to the revoked tokens table"""

        rev_token_id = uuid4()
        db.save_data(
            DbConfig.ADD_REV_TOKEN,
            (rev_token_id, 
            rev_token_jti, 
            rev_token_exp)
        )

    def change_password(self, user_id, new_password):
        """Change password of the user."""

        new_password = hashlib.sha256(new_password.encode()).hexdigest()
        db.save_data(
            DbConfig.CHANGE_PASSWORD,
            ( new_password, "True", user_id )
        )

    def check_token_in_db(self, jti):
        """Check jwt jti in db"""

        token_present = db.fetch_data(
            DbConfig.FETCH_REV_TOKEN,
            (jti,)
        )

        return token_present != ()

    def check_default_pwd_changed(self):
        """Checks whether the default password is changed and profile info is filled or not."""

        return True if (self.user_data['is_def_pwd_changed'] == 1) else False
