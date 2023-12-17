import pytest

from utils.common_helpers import display_table
from config.prints.prints import Prints
from views.approve_dose_info import ApproveDoseInfoViews

@pytest.fixture
def obj_approve_dose(mocker):
    mock = mocker.Mock()
    mocker.patch('views.approve_dose_info.ApproveDoseControllers', return_value = mock)
    mocker.patch('views.approve_dose_info.DoseControllers', return_value = mock)
    return ApproveDoseInfoViews(1)


class TestApproveDoseInfoViews:

    def test_approve_dose_info_menu(self, obj_approve_dose, mocker):
        mocker.patch('builtins.input', side_effect = ['1', '2', '4', '3'])
        mocker.patch.object(obj_approve_dose,'approve_dose_info')
        return_val = obj_approve_dose.approve_dose_info_menu()

        assert return_val is None

    @pytest.mark.parametrize('choice', [('1'),('2')])
    def test_display_info_to_approve_no_data(self, choice, capsys, mocker, obj_approve_dose):
        obj_approve_dose.choice = choice
        mocker.patch.object(obj_approve_dose.approve_dose_controllers_obj, 'show_info_to_approve', lambda a: None)
        return_val = obj_approve_dose.display_info_to_approve()
        captured = capsys.readouterr()
        assert Prints.DATA_NOT_FOUND in captured.out
        assert return_val is False

    @pytest.mark.parametrize('choice', [('1'),('2')])
    def test_display_info_to_approve_data(self, mocker, choice, obj_approve_dose):
        obj_approve_dose.choice = choice
        mocker.patch.object(obj_approve_dose.approve_dose_controllers_obj, 'show_info_to_approve', lambda a: "Data")
        mock_val = mocker.patch('views.approve_dose_info.display_table')
        return_val = obj_approve_dose.display_info_to_approve()
        mock_val.assert_called()
        assert return_val == "Data"

    def test_approve_dose_info_no_data(self, mocker, obj_approve_dose):
        mocker.patch.object(obj_approve_dose, 'display_info_to_approve', return_value = None)
        return_val = obj_approve_dose.approve_dose_info()
        assert return_val is None

    def test_approve_dose_info_no_approval_id(self, mocker, obj_approve_dose):
        mocker.patch.object(obj_approve_dose, 'display_info_to_approve', return_value = None)
        mocker.patch.object(obj_approve_dose, 'get_approval_id', return_value = None)
        return_val = obj_approve_dose.approve_dose_info()
        assert return_val is None

    def test_approve_dose_info_data(self, capsys, mocker, obj_approve_dose):
        mocker.patch.object(obj_approve_dose, 'display_info_to_approve', return_value = "Data")
        mocker.patch.object(obj_approve_dose, 'get_approval_id', return_value = "Id")
        mocker.patch('builtins.input', lambda a: 'Y')
        obj_approve_dose.choice = '1'
        return_val = obj_approve_dose.approve_dose_info()
        captured = capsys.readouterr()
        assert Prints.APPROVAL_SUCCESS in captured.out
        assert return_val is None

    def test_view_approved_details_no_data(self, capsys, obj_approve_dose):
        obj_approve_dose.dose_controllers_obj.fetch_approved_info.return_value = None
        obj_approve_dose.view_approved_details()
        captured = capsys.readouterr()
        assert "Currently, No Approved Data!" in captured.out
    
    def test_view_approved_details_data(self, mocker, obj_approve_dose):
        obj_approve_dose.dose_controllers_obj.fetch_approved_info.return_value = "Data"
        mock = mocker.patch('views.approve_dose_info.display_table')
        obj_approve_dose.view_approved_details()
        mock.assert_called_once()

    def test_get_approval_id_positive(self, mocker, obj_approve_dose):
        mocker.patch('builtins.input', lambda a: 1)
        mock_data = [(1,"")]
        return_val = obj_approve_dose.get_approval_id(mock_data)
        assert return_val == 1

    def test_get_approval_id_negative(self, mocker, obj_approve_dose):
        mocker.patch('builtins.input', lambda a: 1)
        mock_data = [('1',"")]
        return_val = obj_approve_dose.get_approval_id(mock_data)
        assert return_val is False

    def test_get_approval_id_exception(self, capsys, mocker, obj_approve_dose):
        mocker.patch('builtins.input', lambda a: "abc")
        return_val = obj_approve_dose.get_approval_id("")
        captured = capsys.readouterr()
        assert Prints.ENTER_VALID_INPUT in captured.out
        assert return_val is False