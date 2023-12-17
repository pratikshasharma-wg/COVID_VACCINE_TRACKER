from utils.common_helpers import display_table
from utils.input_validators import add_valid_vaccine
from config.prints.prints import Prints
from config.prompts.prompts import PromptsConfig
from controllers.vaccine_controllers import VaccineControllers

class VaccineViews:
    '''
        Class that contains methods to perform various operations on vaccines
    '''

    def __init__(self) -> None:
        self.vaccine_controller_obj = VaccineControllers()


    def add_vaccine(self) -> None:
        '''
            This method adds a new vaccine to the vaccines table
        '''
        vacc_name = add_valid_vaccine()

        result = (self.vaccine_controller_obj.create_vaccine(vacc_name))

        if result:
            print(Prints.VACCINE_ADDED_SUCCESSFULLY)
        else:
            print(Prints.VACCINE_ALREADY_EXISTS)


    def view_vaccines(self) -> None:
        '''
            This method is used to view all the vaccines
        '''
        data =  self.vaccine_controller_obj.show_vaccines()

        if data:
            display_table(data, ["Vaccine ID", "Vaccine Name"])
        else:
            print(Prints.NO_VACCINE_FOUND)


    def get_vaccine_name(self):
        '''
            This method is used to list all the vaccines and then returns vaccine name selected based on vaccine id
        '''
        while True:
            self.view_vaccines()
            vaccine_id = input(PromptsConfig.ENTER_VACCINE_ID)
            vaccine_name = self.vaccine_controller_obj.is_vaccine_present(int(vaccine_id))

            if vaccine_name:
                return vaccine_name
            else:
                print(Prints.ENTER_VALID_VACCINE_ID)
