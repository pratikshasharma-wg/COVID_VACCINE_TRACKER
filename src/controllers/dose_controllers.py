from datetime import date

from config.queries.db_queries import DbConfig
from database.database_operations import db


class DoseControllers:
    '''
        This class contains methods to perform various operations related to dose details.
    '''
    
    def __init__(self, user_id) -> None:
        self.user_id = user_id


    def fetch_dose_info(self) -> list:
        """ This method is used to fetch dose details of an employee from the database. """

        data = db.fetch_data(DbConfig.FETCH_DOSE_1_DETAILS, (self.user_id,))
        return data


    def fetch_vacc_status(self) -> int:
        """ This method is used to fetch vaccination status of an employee. """

        num = db.fetch_data(DbConfig.FETCH_VACC_STATUS, (self.user_id,))
        return num


    def add_dose_info(
        self, vaccine_name: str, dose_1_date: date, dose_1_cid: str
    ) -> None:
        """ This method is used to add dose details by an employee. """

        db.save_data(
            DbConfig.ADD_DOSE_DETAILS,
            (
                self.user_id,
                vaccine_name,
                1,
                dose_1_date,
                dose_1_cid,
            ),
        )
        db.save_data(
            DbConfig.ADD_TO_ADMIN_APPROVAL,
            (
                self.user_id,
                1,
                dose_1_cid,
            ),
        )


    def update_dose_info(self, vaccine_name: str, dose_2_date, dose_2_cid) -> None:
        """ This method is used to update the dose 2 details by an employee if already vaccinated with dose 1. """

        db.save_data(
            DbConfig.ADD_DOSE_DETAILS,
            (
                self.user_id,
                vaccine_name,
                2,
                dose_2_date,
                dose_2_cid,
            ),
        )
        db.save_data(
            DbConfig.ADD_TO_ADMIN_APPROVAL,
            (
                self.user_id,
                2,
                dose_2_cid,
            ),
        )


    def fetch_approved_info(self) -> bool:
        """ This method is used to fetch approved dose details. """

        data = db.fetch_data(DbConfig.APPROVED_DATA)
        return data


    def check_id_present(self, id: int) -> bool:
        """ This method is used to check if a particular certificate id is already present in the database. """

        db_id = db.fetch_data(DbConfig.IS_DOSE_ID_ALREADY_PRESENT, (id,))
        if db_id:
            return True
        else:
            return False