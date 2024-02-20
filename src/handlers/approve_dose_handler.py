from database.database_operations import db
from config.queries.db_queries import DbConfig
from utils.exceptions import NoDataError


class ApproveDoseHandler:

    def get_list_to_approve(self):

        data = db.fetch_data(DbConfig.FETCH_APPROVAL_DATA)
        if not data:
            raise NoDataError(204, "No Content", "Users list is empty")
        
        return data


    def approve_info(self, approval_id):

        data = db.fetch_data(DbConfig.FETCH_APPROVAL_DATA)

        for user in data:
            if user["approval_id"] == approval_id:
                break
        else:
            raise NoDataError(204, "No Content", "Incorrect approval id!!!")

        db.save_data(DbConfig.APPROVE_DOSE_INFO, (approval_id,))
