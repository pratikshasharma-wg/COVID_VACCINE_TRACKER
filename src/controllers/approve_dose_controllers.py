from database.database_operations import db
from config.queries.db_queries import DbConfig


class ApproveDoseControllers:

    def __init__(self) -> None:
        pass

    def show_info_to_approve(self, query) -> bool:

        data = db.fetch_data(query)
        print("4")
        return data
    
    def approve_info(self, approval_id : int) -> None:
        db.save_data(
            DbConfig.APPROVE_DOSE_INFO,
            (approval_id,)
        )