import pytest

from views.auth import AuthViews
from config.prints.prints import Prints

@pytest.fixture
def obj_auth_views(mocker):
    mock_obj = mocker.Mock()
    mocker.patch('views.auth.AuthControllers', return_value = mock_obj)
    auth_obj = AuthViews()
    return auth_obj

class TestAuthViews:

    def test_start_invalid(self, capsys, obj_auth_views, mocker):
        mocker.patch('builtins.input', side_effect = ['3', '2'])
        obj_auth_views.start()
        captured = capsys.readouterr()
        assert Prints.ENTER_VALID in captured.out

    def test_start_valid(self, mocker, obj_auth_views):
        mocker.patch('builtins.input', side_effect = ['1', '2'])
        mocker.patch.object(obj_auth_views, 'login')
        obj_auth_views.start()
        obj_auth_views.login.assert_called_once()

    # def test_login_valid(self, obj_auth_views, capsys, mocker):
    #     mocker.patch('builtins.input', lambda a: "abc")
    #     mocker.patch('maskpass.askpass', lambda a: "123")
    #     mock_obj = mocker.patch('hashlib.sha256')
    #     mock_obj.hexdigest.return_value = "123"
    #     mocker.patch.object(obj_auth_views.auth_controller_obj, 'validate_user', return_value = True)
    #     mocker.patch.object(obj_auth_views, 'role_of_user')
    #     obj_auth_views.login()
    #     captured = capsys.readouterr()
    #     assert obj_auth_views.__login_attempts == 3
        
    def test_role_of_user_admin(self, obj_auth_views, mocker):
        user_info = [(1,"abc", "123", "Admin")]
        mock_obj = mocker.Mock()
        mocker.patch('views.auth.AdminViews', mock_obj)
        mocker.patch.object(mock_obj, 'admin_menu')
        return_val = obj_auth_views.role_of_user(user_info)
        assert return_val is True

    def test_role_of_user_employee(self, obj_auth_views, mocker):
        user_info = [(1,"abc", "123", "Employee")]
        mock_obj = mocker.Mock()
        mocker.patch('views.auth.EmployeeViews', mock_obj)
        mocker.patch.object(mock_obj, 'emp_menu')
        return_val = obj_auth_views.role_of_user(user_info)
        assert return_val is True

    def test_role_of_user_invalid(self, mocker,obj_auth_views):
        user_info = [(1,"abc","123", "invalid")]
        return_val = obj_auth_views.role_of_user(user_info)
        assert return_val is False