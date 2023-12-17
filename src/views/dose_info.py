import logging
from datetime import datetime

from utils.common_helpers import is_future_date
from utils.common_helpers import check_date_diff
from utils.input_validators import input_choice, input_valid_date, input_valid_cid
from config.prints.prints import Prints
from config.prompts.prompts import PromptsConfig
from controllers.dose_controllers import DoseControllers
from views.vaccines import VaccineViews

logger = logging.getLogger('dose_info')

class DoseInfoViews:
    '''
        Class that contains methods to input and update dose details
    '''
    def __init__(self, user_id) -> None:
        self.user_id = user_id
        self.vaccine_obj = VaccineViews()
        self.dose_controller_obj = DoseControllers(self.user_id)


    def update_dose_info(self, vacc_status : int) -> None:
        ''' This method is used to get and update vaccination details based on vaccination status'''

        self.vacc_status = vacc_status
        if self.vacc_status == 0:
            self.update_dose_1_info()
        elif self.vacc_status == 1:
            self.update_dose_2_info()
        else:
            print(Prints.STATUS_ALREADY_UPTODATE)


    def update_dose_1_info(self) -> None:
        ''' This method updates dose 1 details and asks to update dose 2 details also'''

        if self.get_dose_1_info():
            self.dose_controller_obj.add_dose_info(self.vaccine_name, self.dose_1_date, self.dose_1_cid)
            ask_for_dose_2 = input_choice(PromptsConfig.ASK_FOR_DOSE_2_DETAILS)
            
            if ask_for_dose_2:
                self.update_dose_2_info()


    def update_dose_2_info(self) -> None:
        '''This method updates dose 2 details if time duration between both doses is greater than 60 days'''

        self.dose_1_info = self.dose_controller_obj.fetch_dose_info()[0]
        self.dose_1_date = self.dose_1_info[4]
        self.vaccine_name = self.dose_1_info[2]
      
        if not check_date_diff((datetime.now()).strftime("%d/%m/%Y"), self.dose_1_date ):
            print(Prints.CANNOT_UPDATE_DOSE2)
            return
        if self.get_dose_2_info():
            self.dose_controller_obj.update_dose_info(self.vaccine_name, self.dose_2_date, self.dose_2_cid)


    def get_dose_1_info(self) -> bool:
        '''
            This method inputs the dose 1 details and asks to update the details
        '''
        while True:

            self.vaccine_name = self.vaccine_obj.get_vaccine_name()
            self.dose_1_date = input_valid_date(PromptsConfig.ENTER_DOSE_1_DATE)
            if is_future_date(self.dose_1_date):
                print(Prints.FUTURE_DATE_MSG)
                continue

            self.dose_1_cid = input_valid_cid(PromptsConfig.ENTER_DOSE_1_CID)
            if not self.is_acceptable_id(self.dose_1_cid):
                print(Prints.CID_ALREADY_EXISTS)
                continue

            return input_choice(PromptsConfig.ASK_APPROVAL)

            
    def get_dose_2_info(self) -> bool:
        ''' 
            This method inputs the dose 2 date and dose 2 cid  and asks to update the details
        '''

        while True:
            
            self.dose_2_date = input_valid_date(PromptsConfig.ENTER_DOSE_2_DATE)

            if is_future_date(self.dose_2_date):
                print(Prints.FUTURE_DATE_MSG)
                continue
            if not check_date_diff(self.dose_2_date, self.dose_1_date):
                print(Prints.DOSE2_DATE_INVALID)
                continue

            self.dose_2_cid = input_valid_cid(PromptsConfig.ENTER_DOSE_2_CID)
            if not self.is_acceptable_id(self.dose_2_cid):
                print(Prints.CID_ALREADY_EXISTS)
                continue
            
            return input_choice(PromptsConfig.ASK_APPROVAL)
        

    def is_acceptable_id(self, id : int) -> bool:
        ''' This method checks whether the certificate id is already present or not'''

        if (self.dose_controller_obj.check_id_present(id)):
            return False
        else:
            return True