import pytest
import hashlib

from config.prints.prints import Prints
from views.admin import AdminViews
from utils.common_helpers import display_table


@pytest.fixture
def obj_admin_views(mocker):
    mock_user_controller_class = mocker.patch("views.admin.UserControllers")
    mock_vaccine_view_class = mocker.patch("views.admin.VaccineViews")
    mock_approve_dose_class = mocker.patch("views.admin.ApproveDoseInfoViews")
    admin_obj = AdminViews(1)
    admin_obj.user_controller_obj = mock_user_controller_class()
    admin_obj.vaccine_obj = mock_vaccine_view_class()
    admin_obj.approve_dose_info_obj = mock_approve_dose_class()
    return admin_obj


class TestAdminViews:
    def test_admin_menu(self, mocker, obj_admin_views):
        mocker.patch(
            "builtins.input", side_effect=["1", "2", "3", "4", "5", "6", "9", "7"]
        )
        mocker.patch.object(obj_admin_views, "add_new_emp")
        mocker.patch.object(obj_admin_views, "view_emp")
        mocker.patch.object(obj_admin_views.vaccine_obj, "view_vaccines")
        mocker.patch.object(obj_admin_views.vaccine_obj, "add_vaccines")
        mocker.patch.object(
            obj_admin_views.approve_dose_info_obj, "approve_dose_info_menu"
        )
        mocker.patch.object(
            obj_admin_views.approve_dose_info_obj, "view_approved_details"
        )
        return_val = obj_admin_views.admin_menu()
        assert return_val is None

    def test_admin_menu_exit(self, mocker, obj_admin_views):
        mocker.patch("builtins.input", lambda a: "8")
        with pytest.raises(SystemExit):
            obj_admin_views.admin_menu()

    def test_add_new_emp(self, mocker, capsys, obj_admin_views):
        mocker.patch("views.admin.generate_uuid", return_value=1)
        mocker.patch("views.admin.input_valid_email", return_value="abc")
        mocker.patch("views.admin.input_valid_password", return_value="123")
        mock_obj = mocker.Mock()
        mock_obj = mocker.patch("hashlib.sha256", return_value=mock_obj)
        mock_obj.hexdigest.return_value = "123"
        mocker.patch.object(obj_admin_views.user_controller_obj, "create_user")
        obj_admin_views.add_new_emp()
        captured = capsys.readouterr()
        assert Prints.USER_ADDED_SUCCESS in captured.out

    def test_view_emp(self, obj_admin_views, mocker):
        mocker.patch(
            "builtins.input", side_effect=["1", "2", "3", "4", "5", "6", "7", "9", "8"]
        )
        mocker.patch.object(obj_admin_views, "view_all")
        mocker.patch.object(obj_admin_views, "view_by_dose")
        mocker.patch.object(obj_admin_views, "view_by_vaccine")
        mocker.patch.object(obj_admin_views, "view_by_dose_date")
        assert obj_admin_views.view_emp() is None

    def test_view_all_negative(self, capsys, mocker, obj_admin_views):
        mocker.patch.object(
            obj_admin_views.user_controller_obj, "show_all_users", return_value=None
        )
        obj_admin_views.view_all()
        captured = capsys.readouterr()
        assert "No user exists!" in captured.out

    def test_view_all_positive(self, capsys, mocker, obj_admin_views):
        mocker.patch.object(
            obj_admin_views.user_controller_obj, "show_all_users", return_value="abc"
        )
        mock_obj = mocker.patch("views.admin.display_table")
        obj_admin_views.view_all()
        mock_obj.assert_called_once()

    def test_view_by_dose_positive(self, capsys, mocker, obj_admin_views):
        mocker.patch.object(
            obj_admin_views.user_controller_obj,
            "show_users_by_dose",
            return_value="abc",
        )
        mock_obj = mocker.patch("views.admin.display_table")
        obj_admin_views.view_all()
        mock_obj.assert_called_once()

    def test_view_by_dose_negative(self, capsys, mocker, obj_admin_views):
        mocker.patch.object(
            obj_admin_views.user_controller_obj, "show_users_by_dose", return_value=None
        )
        obj_admin_views.view_by_dose(1)
        captured = capsys.readouterr()
        assert Prints.NO_VACC_USER in captured.out

    def test_view_by_vaccine_negative(self, capsys, mocker, obj_admin_views):
        mocker.patch.object(
            obj_admin_views.vaccine_obj, "get_vaccine_name", return_value="abc"
        )
        mocker.patch.object(
            obj_admin_views.user_controller_obj,
            "show_users_by_vaccine",
            return_value=None,
        )
        obj_admin_views.view_by_vaccine()
        captured = capsys.readouterr()
        assert Prints.NO_USER_FOR_THIS_VACCINE in captured.out

    def test_view_by_vaccine_positive(self, capsys, mocker, obj_admin_views):
        mocker.patch.object(
            obj_admin_views.vaccine_obj, "get_vaccine_name", return_value="abc"
        )
        mocker.patch.object(
            obj_admin_views.user_controller_obj,
            "show_users_by_vaccine",
            return_value="abc",
        )
        mock_obj = mocker.patch("views.admin.display_table")
        obj_admin_views.view_by_vaccine()
        mock_obj.assert_called_once()

    def test_view_by_dose_date_positive(self, mocker, obj_admin_views):
        mocker.patch("views.admin.input_valid_date", return_value="1")
        mocker.patch.object(
            obj_admin_views.user_controller_obj,
            "show_users_by_date",
            return_value="abc",
        )
        mock_obj = mocker.patch("views.admin.display_table")
        obj_admin_views.view_by_dose_date(1)
        mock_obj.assert_called_once()

    def test_view_by_dose_date_negative(self, capsys, mocker, obj_admin_views):
        mocker.patch("views.admin.input_valid_date", return_value="1")
        mocker.patch.object(
            obj_admin_views.user_controller_obj, "show_users_by_date", return_value=None
        )
        obj_admin_views.view_by_dose_date(1)
        captured = capsys.readouterr()
        assert Prints.NO_INFO_FOR_DATE in captured.out
