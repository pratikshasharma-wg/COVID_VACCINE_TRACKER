import os
import yaml
current_directory = os.path.dirname(__file__)
FPATH = os.path.join(current_directory, 'prints.yml')


class Prints:
    WELCOME_TO_LOGIN = None
    ENTER_VALID = None
    INVALID_CREDENTIALS = None
    ATTEMPTS_LEFT = None
    NAME_UDATED = None
    GENDER_UPDATED = None
    CHANGE_DEFAULT_PWD = None
    WELCOME_EMP = None
    REMINDER_1 = None
    REMINDER_2 = None
    REMINDER_3 = None
    REMINDER_4 = None
    NAME_UPDATED = None
    WELCOME_MSG = None
    ENTER_VALID = None
    NOT_VACCINATED = None
    VACC_STATUS_1 = None
    VACC_STATUS_2 = None
    REMINDER_1 = None
    REMINDER_2 = None
    REMINDER_3 = None
    REMINDER_4 = None
    DOSE2_DATE_INVALID = None
    ENTER_VALID_DATE = None
    CANNOT_UPDATE_DOSE2 = None
    ENTER_DOSE2_DETAILS = None
    STATUS_UPDATED = None
    ENTER_VALID_NAME = None
    NO_VACC_USER = None
    STATUS_ALREADY_UPTODATE = None
    VACC_NAME = None
    TRY_AGAIN = None
    ENTER_DOSE1_DETAILS = None
    FUTURE_DATE_MSG = None
    APPROVAL_SUCCESS = None
    DATA_NOT_FOUND = None
    USER_ADDED_SUCCESS = None
    NO_INFO_FOR_DATE = None
    CHANGE_DEFAULT_PWD = None
    CONFIRM_PWD_NOT_MATCHED = None
    INVALID_CREDENTIALS = None
    ATTEMPTS_LEFT = None
    ENTER_VALID_EMAIL = None
    SHOW_STATUS_MEANING = None
    NO_USER_FOR_THIS_VACCINE = None
    ENTER_STRONG_PWD = None
    ENTER_VALID_INPUT = None
    ID_NOT_FOUND = None
    WELCOME_EMP = None
    VACCINE_NAME_NOT_SELECTED = None
    CID_ALREADY_EXISTS = None
    WELCOME_TO_LOGIN = None
    NAME_UPDATED = None
    GENDER_UPDATED = None
    VACCINE_ADDED_SUCCESSFULLY = None
    VACCINE_ALREADY_EXISTS = None
    NO_VACCINE_FOUND = None
    ENTER_VALID_VACCINE_ID = None
    NO_APPROVED_DATA = None
    EXITING_APPLICATION = None
    NO_USER_EXISTS = None
    MSG = None

    @classmethod
    def load(cls):
        with open(FPATH, "r") as f:
            data = yaml.safe_load(f)
            cls.WELCOME_MSG = data["WELCOME_MSG"]
            cls.ENTER_VALID = data["ENTER_VALID"]
            cls.NOT_VACCINATED = data["NOT_VACCINATED"]
            cls.VACC_STATUS_1 = data["VACC_STATUS_1"]
            cls.VACC_STATUS_2 = data["VACC_STATUS_2"]
            cls.REMINDER_1 = data["REMINDER_1"]
            cls.REMINDER_2 = data["REMINDER_2"]
            cls.REMINDER_3 = data["REMINDER_3"]
            cls.REMINDER_4 = data["REMINDER_4"]
            cls.DOSE2_DATE_INVALID = data["DOSE2_DATE_INVALID"]
            cls.ENTER_VALID_DATE = data["ENTER_VALID_DATE"]
            cls.CANNOT_UPDATE_DOSE2 = data["CANNOT_UPDATE_DOSE2"]
            cls.ENTER_DOSE2_DETAILS = data["ENTER_DOSE2_DETAILS"]
            cls.STATUS_UPDATED = data["STATUS_UPDATED"]
            cls.ENTER_VALID_NAME = data["ENTER_VALID_NAME"]
            cls.NO_VACC_USER = data["NO_VACC_USER"]
            cls.STATUS_ALREADY_UPTODATE = data["STATUS_ALREADY_UPTODATE"]
            cls.VACC_NAME = data["VACC_NAME"]
            cls.TRY_AGAIN = data["TRY_AGAIN"]
            cls.NO_APPROVED_DATA = data["NO_APPROVED_DATA"]
            cls.ENTER_DOSE1_DETAILS = data["ENTER_DOSE1_DETAILS"]
            cls.FUTURE_DATE_MSG = data["FUTURE_DATE_MSG"]
            cls.APPROVAL_SUCCESS = data["APPROVAL_SUCCESS"]
            cls.DATA_NOT_FOUND = data["DATA_NOT_FOUND"]
            cls.USER_ADDED_SUCCESS = data["USER_ADDED_SUCCESS"]
            cls.NO_INFO_FOR_DATE = data["NO_INFO_FOR_DATE"]
            cls.CHANGE_DEFAULT_PWD = data["CHANGE_DEFAULT_PWD"]
            cls.CONFIRM_PWD_NOT_MATCHED = data["CONFIRM_PWD_NOT_MATCHED"]
            cls.INVALID_CREDENTIALS = data["INVALID_CREDENTIALS"]
            cls.ATTEMPTS_LEFT = data["ATTEMPTS_LEFT"]
            cls.ENTER_VALID_EMAIL = data["ENTER_VALID_EMAIL"]
            cls.SHOW_STATUS_MEANING = data["SHOW_STATUS_MEANING"]
            cls.NO_USER_FOR_THIS_VACCINE = data["NO_USER_FOR_THIS_VACCINE"]
            cls.ENTER_STRONG_PWD = data["ENTER_STRONG_PWD"]
            cls.ENTER_VALID_INPUT = data["ENTER_VALID_INPUT"]
            cls.ID_NOT_FOUND = data["ID_NOT_FOUND"]
            cls.WELCOME_EMP = data["WELCOME_EMP"]
            cls.VACCINE_NAME_NOT_SELECTED = data["VACCINE_NAME_NOT_SELECTED"]
            cls.CID_ALREADY_EXISTS = data["CID_ALREADY_EXISTS"]
            cls.WELCOME_TO_LOGIN = data["WELCOME_TO_LOGIN"]
            cls.NAME_UPDATED = data["NAME_UPDATED"]
            cls.GENDER_UPDATED = data["GENDER_UPDATED"]
            cls.VACCINE_ADDED_SUCCESSFULLY = data["VACCINE_ADDED_SUCCESSFULLY"]
            cls.VACCINE_ALREADY_EXISTS = data["VACCINE_ALREADY_EXISTS"]
            cls.NO_VACCINE_FOUND = data["NO_VACCINE_FOUND"]
            cls.ENTER_VALID_VACCINE_ID = data["ENTER_VALID_VACCINE_ID"]
            cls.EXITING_APPLICATION = data["EXITING_APPLICATION"]
            cls.NO_USER_EXISTS = data["NO_USER_EXISTS"]
            cls.MSG = data["MSG"]

Prints.load()
       