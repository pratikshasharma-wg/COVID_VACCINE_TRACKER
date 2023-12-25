import re
import maskpass
from datetime import datetime, date

from config.prompts.prompts import PromptsConfig
from config.queries.db_queries import DbConfig
from config.prints.prints import Prints
from utils.exceptions import UsernameAlreadyExistsError
from database.database_operations import db


def input_valid_email():
    while True:
        email = input(PromptsConfig.ENTER_USERNAME)
        pattern = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,7}$"
        if re.fullmatch(pattern, email) is not None:
            try:
                if db.fetch_data(DbConfig.FETCH_AUTH_DATA, (email.lower(),)):
                    raise UsernameAlreadyExistsError("Username already present!")
                return email.lower()
            except UsernameAlreadyExistsError as ue:
                print(ue.msg)
        else:
            print(Prints.ENTER_VALID_EMAIL)


def input_valid_password(prompt) -> str:
    while True:
        password = maskpass.askpass(prompt)
        pattern = (
            "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
        )
        if re.fullmatch(pattern, password) is not None:
            return password
        else:
            print(Prints.ENTER_STRONG_PWD)


def add_valid_vaccine() -> str:
    pattern = "^[a-z,A-Z]+"
    while True:
        vaccine_name = input("Enter vaccine name: ").strip()
        if re.match(pattern, vaccine_name):
            return vaccine_name.lower()
        else:
            print("Enter valid vaccine name!")


def input_name() -> str:
    pattern = "^[a-z,A-Z ]{1,20}$"
    while True:
        name = input(PromptsConfig.ENTER_NAME).strip()
        if re.match(pattern, name):
            return name.lower()
        else:
            print(
                "Name should be alphabetic and min 1 and max 20 words in length only!"
            )


def input_gender() -> str:
    while True:
        gender = input(PromptsConfig.ENTER_GENDER)
        if gender.lower() == "male" or gender.lower() == "female":
            return gender.lower()
        print(Prints.ENTER_VALID)


def input_valid_date(prompt) -> date:
    while True:
        try:
            date = input(prompt)
            datetime.strptime(date, "%d/%m/%Y").date()
            return date
        except Exception:
            print("Enter Valid date in dd/mm/yy format!")


def input_valid_cid(prompt) -> str:
    pattern = "^([A-Z])[0-9]{2}$"
    while True:
        cid = input(prompt)
        if re.match(pattern, cid):
            return cid
        print("Enter Valid CID!   For eg. A11")


def input_choice(prompt) -> bool:
    while True:
        if_update = input(prompt)
        if if_update == "1":
            return True
        elif if_update == "2":
            return False
        else:
            print(Prints.ENTER_VALID)
