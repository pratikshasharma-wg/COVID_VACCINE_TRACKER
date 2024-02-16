from database.database_operations import db
from config.queries.db_queries import DbConfig
from utils.exceptions import NoDataError


class ApproveDoseHandler:

    def get_list_to_approve(self, dose_num):

        data = db.fetch_data(DbConfig.FETCH_APPROVAL_DATA, (dose_num,))
        if data is None:
            return []
        
        return data


    def approve_info(self, approval_id):

        data = db.fetch_data(DbConfig.FETCH_APPROVAL_DATA_ALL)
        for i in data:
            if i[0] == approval_id:
                break
        else:
            raise NoDataError(404, "Not Found", "Incorrect approval id!!!")
        
        db.save_data(DbConfig.APPROVE_DOSE_INFO, (approval_id,))