import logging
from os import system

from config.prints.prints import Prints
from utils.common_helpers import display_table
from config.queries.db_queries import DbConfig
from config.prompts.prompts import PromptsConfig
from controllers.dose_controllers import DoseControllers
from controllers.approve_dose_controllers import ApproveDoseControllers

logger = logging.getLogger('Approve Dose Details')

class ApproveDoseInfoViews:
      
    def __init__(self, user_id) -> None:
        self.user_id = user_id
        self.approve_dose_controllers_obj = ApproveDoseControllers()
        self.dose_controllers_obj = DoseControllers(self.user_id)

    def approve_dose_info_menu(self) -> None:
        ''' It shows the prompt to select whether the admin wants to approve dose 1 details or dose 2 details '''

        self.choice = input(PromptsConfig.APPROVE_DETAILS_PROMPT)

        while self.choice != '3':
            if self.choice == '1' or self.choice == '2':
                self.approve_dose_info()
            else:
                print(Prints.ENTER_VALID_INPUT)
            self.choice = (input(PromptsConfig.APPROVE_DETAILS_PROMPT))
        system('cls')


    def display_info_to_approve(self) -> bool:
        '''
            It displays all the data needed to be approved by the admin,
            either for dose 1 or dose 2, based on choice.
        '''
        if self.choice == '1' :
            query = DbConfig.FETCH_1APPROVAL_DATA
        else : 
            query = DbConfig.FETCH_2APPROVAL_DATA
        
        data = self.approve_dose_controllers_obj.show_info_to_approve(query)    
        if data:
            display_table(data, ["Approval ID","User ID", "Dose Num", "Dose CID", "Approved"])
            return data
        else:
            print(Prints.DATA_NOT_FOUND) 
            return False
        
    
    def approve_dose_info(self) -> None:
        ''' It is used to approve details of a particular employee, either dose 1 or dose 2 '''

        data = self.display_info_to_approve()
        if not data :
            return

        approval_id = self.get_approval_id(data)
        if not approval_id:
            return 

        response = input(PromptsConfig.ASK_APPROVAL) 
            
        if response.upper() == 'Y':
            self.approve_dose_controllers_obj.approve_info(approval_id)
            logger.info('Dose {} details approved for approval_id {}'.format(self.choice, approval_id))
            print(Prints.APPROVAL_SUCCESS)


    def view_approved_details(self) -> None:
        ''' It is used to view all the approved details '''

        data = self.dose_controllers_obj.fetch_approved_info()

        if not data:
            print(Prints.NO_APPROVED_DATA)
        else:
            display_table(
                data, 
                ["Approval ID", "User ID", "Dose Number" "Dose CID", "Approved"]
            )


    def get_approval_id(self, data : list) -> bool:
        ''' It checks whether the user id, whose details to be approved, is valid or not '''

        try:
            approval_id = int(input(PromptsConfig.ASK_APPROVAL_ID))
        except Exception:
            print(Prints.ENTER_VALID_INPUT)
            return False
        
        for i in data:
            if i[0] == approval_id :
                break
        else : 
            print(Prints.ID_NOT_FOUND)
            return False
        
        return approval_id