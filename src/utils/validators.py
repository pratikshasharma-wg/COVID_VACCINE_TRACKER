import re


class Validator:
    @staticmethod
    def check_username(username):
        pattern = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,7}$"
        return username if re.fullmatch(pattern, username) else None
