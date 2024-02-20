import yaml

FPATH = "src\\config\\Queries\\db_queries.yml"


class DbConfig:
    CREATE_AUTH_TABLE = None
    CREATE_USER_DETAILS_TABLE = None
    CREATE_DOSE_DETAILS_TABLE = None
    CREATE_ADMIN_APPROVAL_TABLE = None
    CREATE_VACCINE_TABLE = None
    USER_DATA = None
    UPDATE_PWD = None
    ADD_USER = None
    FETCH_BY_DOSE = None
    FETCH_BY_VACCINE = None
    FETCH_BY_DOSE1_DATE = None
    FETCH_BY_DOSE2_DATE = None
    ADD_VACCINE = None
    APPROVE_DOSE_INFO = None
    FETCH_APPROVAL_DATA = None
    FETCH_2APPROVAL_DATA = None
    FETCH_VACC_STATUS = None
    FETCH_DOSE_1_DETAILS = None
    FETCH_VACCINE_DETAILS = None
    ADD_DOSE_DETAILS = None
    ADD_TO_ADMIN_APPROVAL = None
    UPDATE_ADMIN_APPROVAL = None
    UPDATE_DOSE2_DETAILS = None
    UPDATE_ADMIN_APPROVAL2 = None
    SELECT_DOSE1_DATE = None
    UPDATE_NAME = None
    UPDATE_GENDER = None
    FETCH_APPROVED_DATA = None
    ADD_USER_DETAILS = None
    FETCH_AUTH_DATA = None
    FETCH_VACCINE_NAME = None
    FETCH_USER_DETAILS = None
    FETCH_USERS_BY_DATE = None
    IS_DOSE_ID_ALREADY_PRESENT = None
    FETCH_VACCINE = None
    FETCH_DOSE_DETAILS_BY_DOSE_CID = None
    FETCH_DOSE_DETAILS_BY_DOSE2CID = None
    FETCH_DOSE_0_EMPLOYEES = None
    FETCH_DOSE_1_EMPLOYEES = None
    FETCH_USER = None
    FETCH_APPROVAL_DATA_ALL = None
    FETCH_SPECIFIC_VACCINE = None
    FETCH_PROFILE = None
    FETCH_USER_DOSE_2 = None

    @classmethod
    def load(cls):
        with open(FPATH, "r") as f:
            data = yaml.safe_load(f)
            cls.CREATE_AUTH_TABLE = data["CREATE_AUTH_TABLE"]
            cls.CREATE_USER_DETAILS_TABLE = data["CREATE_USER_DETAILS_TABLE"]
            cls.CREATE_DOSE_DETAILS_TABLE = data["CREATE_DOSE_DETAILS_TABLE"]
            cls.CREATE_ADMIN_APPROVAL_TABLE = data["CREATE_ADMIN_APPROVAL_TABLE"]
            cls.CREATE_VACCINE_TABLE = data["CREATE_VACCINE_TABLE"]
            cls.USER_DATA = data["USER_DATA"]
            cls.UPDATE_PWD = data["UPDATE_PWD"]
            cls.ADD_USER = data["ADD_USER"]
            cls.FETCH_BY_DOSE = data["FETCH_BY_DOSE"]
            cls.FETCH_BY_VACCINE = data["FETCH_BY_VACCINE"]
            cls.FETCH_BY_DOSE1_DATE = data["FETCH_BY_DOSE1_DATE"]
            cls.FETCH_BY_DOSE2_DATE = data["FETCH_BY_DOSE2_DATE"]
            cls.ADD_VACCINE = data["ADD_VACCINE"]
            cls.APPROVE_DOSE_INFO = data["APPROVE_DOSE_INFO"]
            cls.FETCH_APPROVAL_DATA = data["FETCH_APPROVAL_DATA"]
            cls.FETCH_2APPROVAL_DATA = data["FETCH_2APPROVAL_DATA"]
            cls.FETCH_VACC_STATUS = data["FETCH_VACC_STATUS"]
            cls.FETCH_DOSE_1_DETAILS = data["FETCH_DOSE_1_DETAILS"]
            cls.FETCH_VACCINE_DETAILS = data["FETCH_VACCINE_DETAILS"]
            cls.ADD_DOSE_DETAILS = data["ADD_DOSE_DETAILS"]
            cls.ADD_TO_ADMIN_APPROVAL = data["ADD_TO_ADMIN_APPROVAL"]
            cls.UPDATE_ADMIN_APPROVAL = data["UPDATE_ADMIN_APPROVAL"]
            cls.UPDATE_DOSE2_DETAILS = data["UPDATE_DOSE2_DETAILS"]
            cls.UPDATE_ADMIN_APPROVAL2 = data["UPDATE_ADMIN_APPROVAL"]
            cls.SELECT_DOSE1_DATE = data["SELECT_DOSE1_DATE"]
            cls.UPDATE_NAME = data["UPDATE_NAME"]
            cls.UPDATE_GENDER = data["UPDATE_GENDER"]
            cls.FETCH_APPROVED_DATA = data["FETCH_APPROVED_DATA"]
            cls.ADD_USER_DETAILS = data["ADD_USER_DETAILS"]
            cls.FETCH_AUTH_DATA = data["FETCH_AUTH_DATA"]
            cls.FETCH_VACCINE_NAME = data["FETCH_VACCINE_NAME"]
            cls.FETCH_USER_DETAILS = data["FETCH_USER_DETAILS"]
            cls.IS_DOSE_ID_ALREADY_PRESENT = data["IS_DOSE_ID_ALREADY_PRESENT"]
            cls.FETCH_VACCINE = data["FETCH_VACCINE"]
            cls.FETCH_DOSE_DETAILS_BY_DOSE_CID = data["FETCH_DOSE_DETAILS_BY_DOSE_CID"]
            cls.FETCH_DOSE_DETAILS_BY_DOSE2CID = data["FETCH_DOSE_DETAILS_BY_DOSE2CID"]
            cls.FETCH_DOSE_0_EMPLOYEES = data['FETCH_DOSE_0_EMPLOYEES']
            cls.FETCH_DOSE_1_EMPLOYEES = data['FETCH_DOSE_1_EMPLOYEES']
            # cls.FETCH_DOSE_2_EMPLOYEES = data['FETCH_DOSE_2_EMPLOYEES']
            cls.FETCH_USER = data['FETCH_USER']
            cls.FETCH_APPROVAL_DATA_ALL = data['FETCH_APPROVAL_DATA_ALL']
            cls.FETCH_SPECIFIC_VACCINE = data['FETCH_SPECIFIC_VACCINE']
            cls.FETCH_USERS_BY_DATE = data['FETCH_USERS_BY_DATE']
            cls.FETCH_PROFILE = data['FETCH_PROFILE']
            cls.FETCH_USER_DOSE_2 = data['FETCH_USER_DOSE_2']

DbConfig.load()
