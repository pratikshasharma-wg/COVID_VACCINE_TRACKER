from database.database_operations import db
from config.queries.db_queries import DbConfig
from handlers.approve_dose_handler import ApproveDoseHandler


class ApproveDoseControllers:
    '''
        Class that contains methods to perform opertions related to approval of vaccination details.
    '''

    def __init__(self) -> None:
        self.approve_dose_handler = ApproveDoseHandler()


    def show_info_to_approve(self, query) -> bool:
        """ 
            This method is used to show the data to be approved by admin. 
        """

        data = db.fetch_data(query)
        return data


    def approve_info(self, approval_id: int) -> None:
        """ 
            This method is used to approve the details by admin. 
        """

        db.save_data(DbConfig.APPROVE_DOSE_INFO, (approval_id,))