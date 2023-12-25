import pytest

from views.employee import EmployeeViews
from config.prints.prints import Prints


@pytest.fixture
def mock_user_controller_class(mocker):
    return mocker.patch("views.employee.UserControllers")


@pytest.fixture
def mock_dose_info_views_class(mocker):
    return mocker.patch("views.employee.DoseInfoViews")


@pytest.fixture
def mock_dose_controller_class(mocker):
    return mocker.patch("views.employee.DoseControllers")


@pytest.fixture
def mock_obj_employee_views(
    mocker,
    mock_user_controller_class,
    mock_dose_info_views_class,
    mock_dose_controller_class,
):
    return EmployeeViews(1)


class TestEmployeeViews:
    def test_emp_menu(
        self, mocker, mock_dose_info_views_class, mock_obj_employee_views
    ):
        mock_obj_employee_views.vacc_status = 1
        mocker.patch.object(mock_obj_employee_views, "show_reminders")
        mocker.patch("builtins.input", side_effect=["1", "2", "3", "6", "4"])
        mocker.patch.object(mock_obj_employee_views, "check_vacc_status")
        mocker.patch.object(
            mock_dose_info_views_class(), "update_dose_info", lambda a: None
        )
        mocker.patch.object(mock_obj_employee_views, "update_profile")
        return_value = mock_obj_employee_views.emp_menu()
        assert return_value is None

    def test_emp_menu_system_exit(self, mocker, mock_obj_employee_views, capsys):
        mocker.patch("builtins.input", return_value="5")
        mocker.patch.object(mock_obj_employee_views, "show_reminders")
        with pytest.raises(SystemExit):
            mock_obj_employee_views.emp_menu()

    @pytest.mark.parametrize(
        "inputs, reminders",
        [
            ([(0, "")], Prints.REMINDER_1),
            ([(1, "")], Prints.REMINDER_2),
            ([(1, "")], Prints.REMINDER_3),
            ([(2, "")], Prints.REMINDER_4),
        ],
    )
    def test_show_reminders(
        self, inputs, mocker, reminders, capsys, mock_obj_employee_views
    ):
        mocker.patch.object(
            mock_obj_employee_views.dose_controller_obj,
            "fetch_vacc_status",
            return_value=inputs,
        )
        if inputs[0][0] == 1:
            mocker.patch.object(
                mock_obj_employee_views.dose_controller_obj,
                "fetch_dose_info",
                lambda a: "date",
            )
            mocker.patch("views.employee.check_date_diff", side_effect=[True, False])
        mock_obj_employee_views.show_reminders()
        captured = capsys.readouterr()
        assert reminders in captured.out

    def test_update_profile(
        self, mock_user_controller_class, capsys, mocker, mock_obj_employee_views
    ):
        mocker.patch("views.employee.input_name")
        mock_obj_user_controller = mock_user_controller_class()
        mock_obj_employee_views.user_controller_obj = mock_obj_user_controller
        mocker.patch.object(mock_obj_employee_views.user_controller_obj, "update_name")
        mocker.patch("views.employee.input_gender")
        mocker.patch.object(mock_obj_employee_views.user_controller_obj, "update_name")
        mock_obj_employee_views.update_profile()
        captured = capsys.readouterr()
        assert "Name updated successfully!\n" in captured.out
        assert "Gender updated successfully!\n" in captured.out

    @pytest.mark.parametrize(
        "vacc_status, output",
        [
            ([(0, "")], Prints.NOT_VACCINATED),
            ([(1, "")], Prints.VACC_STATUS_1),
            ([(2, "")], Prints.VACC_STATUS_2),
        ],
    )
    def test_check_vacc_status_1(
        self, mocker, vacc_status, output, capsys, mock_obj_employee_views
    ):
        mocker.patch.object(
            mock_obj_employee_views.dose_controller_obj,
            "fetch_vacc_status",
            return_value=vacc_status,
        )
        mock_obj_employee_views.check_vacc_status()
        captured = capsys.readouterr()
        assert output in captured.out
