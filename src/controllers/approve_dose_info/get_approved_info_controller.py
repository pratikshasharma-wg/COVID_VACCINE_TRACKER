from utils.exceptions import CustomException
from handlers.approve_dose_handler import ApproveDoseHandler


class GetApprovedInfoController:
    '''
        Class that contains methods to get approved info.
    '''

    def __init__(self) -> None:
        self.approve_dose_handler = ApproveDoseHandler()


    def show_info_to_approve(self, dose_num) -> bool:
        """ 
            This method is used to show the data to be approved by admin. 
        """

        try:
            self.approve_dose_handler.get_list_to_approve(dose_num)

        except CustomException as e:
            return e.dump(), e.code