"""This module contains prompts to load for the project"""
# third party imports
import os
import yaml
current_directory = os.path.dirname(__file__)
FPATH = os.path.join(current_directory, 'prompts.yml')


class PromptsConfig:
    """
    This class contains method to load all the prompts
    ...
    Methods
    -------
    load():
        This method loads all the project prompts from the yaml file
    """

    ATTEMPTS_MESSAGE = None
    ATTEMPTS_EXHAUSTED = None
    EXIT_SYSTEM_PROMPT = None
    ENTER_USERNAME = None
    ENTER_PASSWORD = None
    INVALID_LOGIN = None
    ENTER_NAME = None
    ENTER_VACCINE_ID = None
    LOGIN_PROMPT = None
    GET_USERNAME = None
    GET_PWD = None
    NEW_PWD = None
    ADMIN_PROMPT = None
    LOGIN_PROMPT = None
    GET_USERNAME = None
    GET_PWD = None
    NEW_PWD = None
    CONFIRM_NEW_PWD = None
    ASSIGN_USERNAME = None
    ASSIGN_DEFAULT_PWD = None
    GET_VACCINE = None
    VALID_CHOICE = None
    ASK_APPROVAL_ID = None
    APPROVE_DETAILS_PROMPT = None
    ASK_APPROVAL = None
    GET_DATE = None
    VALID_VACCINE = None
    VIEW_VACC_STATUS_PROMPT = None
    EMPLOYEE_PROMPT = None
    UPDATE_VACC_STATUS = None
    GET_NAME = None
    UPDATE_DETAILS_PROMPT1 = None
    UPDATE_DETAILS_PROMPT2 = None
    ENTER_GENDER = None
    GET_DOSE_CID = None
    GET_DOSE2_CID = None
    ENTER_USERNAME = None
    EMPTY_NAME_ERROR = None
    NAME_ALREADY_EXISTS = None
    NOT_ALPHABETIC_NAME = None
    ENTER_IN_VALID_DOSE_ID_FORMAT = None
    ENTER_DOSE_1_DATE = None
    ENTER_DOSE_2_DATE = None
    ENTER_DOSE_1_CID = None
    ENTER_DOSE_2_CID = None
    ASK_FOR_DOSE_2_DETAILS = None

    @classmethod
    def load(cls) -> None:
        """
        This method loads all the data from yaml
        Parameters = cls
        Return Type = None
        """
        with open("src/config/prompts/prompts.yml", "r") as file:
            data = yaml.safe_load(file)

            cls.ATTEMPTS_MESSAGE = data["ATTEMPTS_MESSAGE"]
            cls.ATTEMPTS_EXHAUSTED = data["ATTEMPTS_EXHAUSTED"]
            cls.EXIT_SYSTEM_PROMPT = data["EXIT_SYSTEM_PROMPT"]
            cls.ENTER_USERNAME = data["ENTER_USERNAME"]
            cls.ENTER_NAME = data["ENTER_NAME"]
            cls.ASK_FOR_DOSE_2_DETAILS = data["ASK_FOR_DOSE_2_DETAILS"]
            cls.INVALID_LOGIN = data["INVALID_LOGIN"]
            cls.ENTER_VACCINE_ID = data["ENTER_VACCINE_ID"]
            cls.ADMIN_PROMPT = data["ADMIN_PROMPT"]
            cls.LOGIN_PROMPT = data["LOGIN_PROMPT"]
            cls.GET_USERNAME = data["GET_USERNAME"]
            cls.ENTER_PWD = data["ENTER_PWD"]
            cls.NEW_PWD = data["NEW_PWD"]
            cls.CONFIRM_NEW_PWD = data["CONFIRM_NEW_PWD"]
            cls.ASSIGN_USERNAME = data["ASSIGN_USERNAME"]
            cls.ASSIGN_DEFAULT_PWD = data["ASSIGN_DEFAULT_PWD"]
            cls.GET_VACCINE = data["GET_VACCINE"]
            cls.VALID_CHOICE = data["VALID_CHOICE"]
            cls.ASK_APPROVAL_ID = data["ASK_APPROVAL_ID"]
            cls.APPROVE_DETAILS_PROMPT = data["APPROVE_DETAILS_PROMPT"]
            cls.ASK_APPROVAL = data["ASK_APPROVAL"]
            cls.GET_DATE = data["GET_DATE"]
            cls.VALID_VACCINE = data["VALID_VACCINE"]
            cls.VIEW_VACC_STATUS_PROMPT = data["VIEW_VACC_STATUS_PROMPT"]
            cls.EMPLOYEE_PROMPT = data["EMPLOYEE_PROMPT"]
            cls.UPDATE_VACC_STATUS = data["UPDATE_VACC_STATUS"]
            cls.GET_NAME = data["GET_NAME"]
            cls.UPDATE_DETAILS_PROMPT1 = data["UPDATE_DETAILS_PROMPT1"]
            cls.UPDATE_DETAILS_PROMPT2 = data["UPDATE_DETAILS_PROMPT2"]
            cls.ENTER_GENDER = data["ENTER_GENDER"]
            cls.GET_DOSE_CID = data["GET_DOSE_CID"]
            cls.GET_DOSE2_CID = data["GET_DOSE2_CID"]
            cls.ENTER_USERNAME = data["ENTER_USERNAME"]
            cls.EMPTY_NAME_ERROR = data["EMPTY_NAME_ERROR"]
            cls.NAME_ALREADY_EXISTS = data["NAME_ALREADY_EXISTS"]
            cls.NOT_ALPHABETIC_NAME = data["NOT_ALPHABETIC_NAME"]
            cls.ENTER_IN_VALID_DOSE_ID_FORMAT = data["ENTER_IN_VALID_DOSE_ID_FORMAT"]
            cls.ENTER_DOSE_1_DATE = data["ENTER_DOSE_1_DATE"]
            cls.ENTER_DOSE_2_DATE = data["ENTER_DOSE_2_DATE"]
            cls.ENTER_DOSE_1_CID = data["ENTER_DOSE_1_CID"]
            cls.ENTER_DOSE_2_CID = data["ENTER_DOSE_2_CID"]

PromptsConfig.load()
