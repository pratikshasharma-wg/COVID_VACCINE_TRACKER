import sys
import time
import hashlib
import logging
from tabulate import tabulate
from os import system

from views.vaccines import VaccineViews
from views.approve_dose_info import ApproveDoseInfoViews
from config.logs.logs import Logs
from config.prints.prints import Prints
from config.prompts.prompts import PromptsConfig
from controllers.user_controllers import UserControllers
from utils.common_helpers import generate_uuid
from utils.generators import list_generator
from utils.common_helpers import display_table
from utils.input_validators import input_valid_email, input_valid_password, input_valid_date

logger = logging.getLogger('admin_menu')

class AdminViews:
    '''
        Class that contains admin menu and various operations that admin can perform
    '''
   
    def __init__(self, user_id) -> None:
        logger.info(Logs.ADMIN_MSG)
        self.user_id = user_id
        self.user_controller_obj = UserControllers()
        self.vaccine_obj = VaccineViews()
        self.approve_dose_info_obj = ApproveDoseInfoViews(self.user_id)
        system('cls')
       

    def admin_menu(self) -> None:  
        """
            Menu function which shows different operations admin can perform.
        """
        admin_choice = input(PromptsConfig.ADMIN_PROMPT)

        while admin_choice != '8':    
            match admin_choice:
                case '1':
                    self.add_new_emp()
                case '2':
                    self.view_emp()
                case '3':
                    self.vaccine_obj.add_vaccine()
                case '4':
                    self.vaccine_obj.view_vaccines()
                case '5':
                    self.approve_dose_info_obj.approve_dose_info_menu()
                case '6':
                    self.approve_dose_info_obj.view_approved_details()
                case '7':
                    system('cls')
                    return None
                case _:
                    print(Prints.ENTER_VALID)
            admin_choice = (input(PromptsConfig.ADMIN_PROMPT))
        sys.exit()


    def add_new_emp(self) -> None:
        '''
            It is used to add new employee into the system by the admin.
        '''
        user_id = generate_uuid()
        username = input_valid_email().lower()
        password = input_valid_password(PromptsConfig.ASSIGN_DEFAULT_PWD)
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        self.user_controller_obj.create_user(user_id, username, hashed_password)

        logger.info("New User Added!")
        print(Prints.USER_ADDED_SUCCESS)   


    def view_emp(self):
        """
            It shows all the filter options on the basis of which admin can view vaccination info of employees.
        """ 
        system('cls')
        while True:
            choice = (input(PromptsConfig.VIEW_VACC_STATUS_PROMPT))
            if choice == '1':
                self.view_all()
            elif choice == '2':
                self.view_by_dose(1)
            elif choice == '3':
                self.view_by_dose(2)
            elif choice == '4':
                self.view_by_dose(0)
            elif choice == '5':
                self.view_by_vaccine()
            elif choice == '6':
                self.view_by_dose_date(1)
            elif choice == '7':
                self.view_by_dose_date(2)
            elif choice == '8':
                system('cls')
                return
            else:
                print(Prints.ENTER_VALID)
                continue


    def view_all(self) -> None:

        data = self.user_controller_obj.show_all_users()
        if data:
            employee_generator = list_generator(data)
            for employees in employee_generator:
                print(tabulate(employees, headers= ["UserID","Email", "Vaccination Status" ]))
                time.sleep(5)
            # display_table(data, ["UserID","Email", "Vaccination Status" ])
        else:
            print("No user exists!")


    def view_by_dose(self,status : int) -> None:

        data = self.user_controller_obj.show_users_by_dose(status)
    
        if data:
            display_table(data, ["User ID", "Username", "Vaccine Name"])   
        else:
            print(Prints.NO_VACC_USER)  
            

    def view_by_vaccine(self):

        vaccine_name = self.vaccine_obj.get_vaccine_name()
        data = self.user_controller_obj.show_users_by_vaccine(vaccine_name)
        if data:
            display_table(data, ["User ID", "Email", "Vaccine Name"])
        else:
            print(Prints.NO_USER_FOR_THIS_VACCINE)


    def view_by_dose_date(self, dose_num : int) -> None:
        if dose_num == 1:
            prompt = PromptsConfig.ENTER_DOSE_1_DATE
        else:
            prompt = PromptsConfig.ENTER_DOSE_2_DATE
        self.date = input_valid_date(prompt)
           
        data = self.user_controller_obj.show_users_by_date(self.date, dose_num)

        if not data:
            print(Prints.NO_INFO_FOR_DATE)
        else:
            display_table(data, ["User ID","email", "Vaccine Name", "Dose Date", "Dose CID"])