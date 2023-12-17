from datetime import date

from config.queries.db_queries import DbConfig
from database.database_operations import db

class DoseControllers:

    def __init__(self, user_id) -> None:
        self.user_id = user_id

    def fetch_dose_info(self) -> list:
        data = db.fetch_data(
            DbConfig.FETCH_DOSE_1_DETAILS,
            (self.user_id,)
        )
        return data
    
    def fetch_vacc_status(self) -> int:
        num = db.fetch_data(
            DbConfig.FETCH_VACC_STATUS,
            (self.user_id,)
        )
        return num

    def add_dose_info(self, vaccine_name : str, dose_1_date : date, dose_1_cid : str) -> None:
        db.save_data(
            DbConfig.ADD_DOSE_DETAILS,(
            self.user_id, 
            vaccine_name,
            1, 
            dose_1_date, 
            dose_1_cid, )
        )
        db.save_data(
            DbConfig.ADD_TO_ADMIN_APPROVAL,(
            self.user_id,
            1,
            dose_1_cid,)
        )
    

    def update_dose_info(self, vaccine_name : str, dose_2_date, dose_2_cid) -> None:
        db.save_data(
            DbConfig.ADD_DOSE_DETAILS,
            (self.user_id,
            vaccine_name,
            2,
            dose_2_date, 
            dose_2_cid,)
        )
        db.save_data(
            DbConfig.ADD_TO_ADMIN_APPROVAL,(
                self.user_id,
                2,
                dose_2_cid,
            )
        )
        
    def fetch_approved_info(self) -> bool:

        data = db.fetch_data(DbConfig.APPROVED_DATA)
        return data
        
    def check_id_present(self, id : int) -> bool:
        db_id = db.fetch_data(DbConfig.IS_DOSE_ID_ALREADY_PRESENT, (id,))
        if db_id:
            return True
        else:
            return False