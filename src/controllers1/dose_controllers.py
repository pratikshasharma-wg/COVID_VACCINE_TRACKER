from handlers.dose_handlers import DoseHandlers


class DoseControllers:
    '''
        This class contains methods to perform various operations related to dose details.
    '''
    
    def __init__(self, user_id) -> None:
        self.user_id = user_id
        self.dose_handler = DoseHandlers()


    def fetch_dose_info(self) -> list:
        """ This method is used to fetch dose details of an employee from the database. """

        try:
            data = self.dose_handler.get_dose_info(self.user_id)
            return data
        except Exception:
            ...


    def fetch_vacc_status(self) -> int:
        """ This method is used to fetch vaccination status of an employee. """
        try:
            num = self.dose_handler.get_vacc_status(self.user_id)
            return num
        except Exception:
            ...


    def add_dose_info(
        self, dose_info: str
        ) :
        """ This method is used to add dose details by an employee. """

        self.dose_handler.add_dose_info(self.user_id, dose_info["vaccine_name"], dose_info["dose_1_date"], dose_info["dose_1_cid"])

        return {
            "message": "Dose details addedd successfully!"
        }, 201


def update_dose_info(self, vaccine_name: str, dose_2_date, dose_2_cid) -> None:
    """ This method is used to update the dose 2 details by an employee if already vaccinated with dose 1. """

    try:
        self.dose_handler.update_dose_info(self.user_id, vaccine_name, dose_2_date, dose_2_cid)
        return {
            "message": "Dose details updated successfully!"
        }
    except Exception:
        ...


    def fetch_approved_info(self) -> bool:
        """ This method is used to fetch approved dose details. """
        try:
            data = self.dose_handler.get_approved_info()
            return data
        except Exception:
            ...


    def check_id_present(self, id: int) -> bool:
        """ This method is used to check if a particular certificate id is already present in the database. """
        try:
            db_id = self.dose_handler.check_id_present(id)
            if db_id:
                return {
                    "message": "User already exists!"
                }
            else:
                return False
        except Exception:
            ...