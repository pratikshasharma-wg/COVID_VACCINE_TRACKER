from pymysql.err import IntegrityError

from database.database_operations import db
from config.queries.db_queries import DbConfig
from utils.exceptions import AlreadyExistsError, NoDataError


class DoseHandlers:

    def get_dose_info(self, user_id):
        
        data = db.fetch_data(DbConfig.FETCH_DOSE_1_DETAILS, (user_id,))

        if data is None:
            return []

        return data

    def get_user_doses(self, user_id):
        data = db.fetch_data(DbConfig.USER_DOSES, (user_id,))
        return data if data is not None else []


    def get_vacc_status(self, user_id):
        
        data = db.fetch_data(DbConfig.FETCH_VACC_STATUS, (user_id,))

        if data is None:
            return []
        
        return data

    def add_dose(self, user_id, vaccine_name, dose_date, dose_cid, dose_number):
        data = db.fetch_data(DbConfig.DOSE_ALREADY, (user_id, dose_number))
        if data:
            raise AlreadyExistsError(409, "Conflict", "Does details already added!")

        try:
            db.save_data(
            DbConfig.ADD_DOSE_DETAILS,
            (
                user_id,
                vaccine_name,
                dose_number,
                dose_date,
                dose_cid,
            ),
            )

            db.save_data(
                DbConfig.ADD_TO_ADMIN_APPROVAL,
                (
                    user_id,
                    dose_number,
                    dose_cid,
                ),
            )
        except IntegrityError:
            raise AlreadyExistsError(409, "Conflict", "Dose Id already exists!!!")



    def add_dose_info(self, user_id, vaccine_name, dose_1_date, dose_1_cid):
        
        data = db.fetch_data(DbConfig.FETCH_USER, (user_id,))
        
        if data:
            raise AlreadyExistsError(409, "Conflict", "Dose details already added!!!")
        
        try:
            db.save_data(
            DbConfig.ADD_DOSE_DETAILS,
            (
                user_id,
                vaccine_name,
                1,
                dose_1_date,
                dose_1_cid,
            ),
            )

            db.save_data(
                DbConfig.ADD_TO_ADMIN_APPROVAL,
                (
                    user_id,
                    1,
                    dose_1_cid,
                ),
            )
        except IntegrityError:
            raise AlreadyExistsError(409, "Conflict", "Dose Id already exists!!!")
        

    def update_dose_info(self, user_id, vaccine_name, dose_date, dose_cid):

        data = db.fetch_data(DbConfig.FETCH_USER_DOSE_2, (user_id,2,))
        
        if data:
            raise AlreadyExistsError(409, "Conflict", "Dose details already added!!!")
        
        try:
            db.save_data(
            DbConfig.ADD_DOSE_DETAILS,
            (
                user_id,
                vaccine_name,
                2,
                dose_date,
                dose_cid,
            ),
            )
            db.save_data(
                DbConfig.ADD_TO_ADMIN_APPROVAL,
                (
                    user_id,
                    2,
                    dose_cid,
                ),
            )
        except IntegrityError:
            raise AlreadyExistsError(409, "Conflict", "Dose Id already exists!!!")
        


    def get_approved_info(self):
        
        data = db.fetch_data(DbConfig.APPROVED_DATA)
        if data is None:
            return []
        
        return data
    

    def check_id_present(self, id):
        
        data = db.fetch_data(DbConfig.IS_DOSE_ID_ALREADY_PRESENT, (id,))
        if data is None:
            return []
        
        return data
        