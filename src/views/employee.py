import sys
import logging
from os import system
from datetime import datetime

from config.prints.prints import Prints
from config.prompts.prompts import PromptsConfig
from views.dose_info import DoseInfoViews
from controllers.user_controllers import UserControllers
from controllers.dose_controllers import DoseControllers
from utils.input_validators import input_name, input_gender
from utils.common_helpers import check_date_diff


logger = logging.getLogger('employee')


class EmployeeViews:
    '''
        Class that contains employee menu and various operations that employee can perform
    '''
    def __init__(self, user_id : int) -> None:
        logger.info('Logs.EMPLOYEE_MSG'.format())
        print(Prints.WELCOME_EMP)
        self.user_id = user_id
        self.user_controller_obj = UserControllers()
        self.dose_info_obj = DoseInfoViews(self.user_id)
        self.dose_controller_obj = DoseControllers(self.user_id)
        system('cls')


    def emp_menu(self) -> None:
        """
            Menu functions which shows different operations an employee can perform.
        """
        self.show_reminders()

        employee_choice = input(PromptsConfig.EMPLOYEE_PROMPT)
        
        while employee_choice != '5':
            match employee_choice:
                case '1':
                    self.check_vacc_status()
                case '2':
                    vacc_status = self.dose_controller_obj.fetch_vacc_status()[0][0]
                    self.dose_info_obj.update_dose_info(vacc_status)
                case '3':
                    self.update_profile()
                case '4':
                    system('cls')
                    return 
                case _:
                    print(Prints.ENTER_VALID)    
            employee_choice = (input(PromptsConfig.EMPLOYEE_PROMPT))
        sys.exit()


    def show_reminders(self):
        """
            It shows reminder when the employee logs in
        """
        vacc_status = self.dose_controller_obj.fetch_vacc_status()[0][0]

        if vacc_status == 0:
            print(Prints.REMINDER_1)

        elif vacc_status == 1:
            self.dose_1_date = self.dose_controller_obj.fetch_dose_info()[0][4]

            if check_date_diff((datetime.now()).strftime("%d/%m/%Y"), self.dose_1_date ):
                print(Prints.REMINDER_2, "\n")
            else:
                print(Prints.REMINDER_3, "\n")

        else:
            print(Prints.REMINDER_4)


    def update_profile(self) -> None:
        '''
            It updates the name and gender of an employee
        '''

        name = input_name()
        self.user_controller_obj.update_name(name, self.user_id)
        print(Prints.NAME_UPDATED)

        gender = input_gender()
        self.user_controller_obj.update_gender(gender, self.user_id)
        print(Prints.GENDER_UPDATED) 

        logger.info('Profile Updated!')  


    def check_vacc_status(self) -> None:
        '''
            This methos prints the vaccination status of an employee
        '''
        vacc_status = self.dose_controller_obj.fetch_vacc_status()[0][0]
        if vacc_status == 2:
            print(Prints.VACC_STATUS_2)
        elif vacc_status == 1:
            print(Prints.VACC_STATUS_1)
        else:
            print(Prints.NOT_VACCINATED)   