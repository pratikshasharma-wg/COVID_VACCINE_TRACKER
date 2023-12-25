import pytest
import hashlib

from controllers.auth_controllers import AuthControllers


@pytest.fixture
def mock_db_fetch_data(mocker):
    return mocker.patch("database.database_operations.db.fetch_data")


@pytest.fixture
def mock_db_save_data(mocker):
    return mocker.patch("database.database_operations.db.save_data")


@pytest.fixture
def mock_employee_views(mocker):
    return mocker.patch("views.employee.EmployeeViews.update_profile")


@pytest.fixture
def mock_hash_pwd(mocker):
    mock_val = mocker.patch("hashlib.sha256", return_val="")
    mock_val.hexdigest.return_value = "hashed_password"
    return mock_val


@pytest.fixture
def mock_change_default_pwd(mocker):
    return mocker.patch.object(AuthControllers, "change_default_pwd", return_value=None)


class TestAuthControllers:
    def test_validate_user_with_valid_credentials(
        self, mock_db_fetch_data, mock_hash_pwd, mock_employee_views
    ):
        instance = AuthControllers()
        email = "test@example.com"
        password = "password123"

        mock_db_fetch_data.return_value = [
            (1, email, "hashed_password", "Admin", "True")
        ]

        result = instance.validate_user(email, password)

        assert result

    def test_validate_user_with_invalid_credentials(
        self, mock_db_fetch_data, mock_hash_pwd, mock_employee_views
    ):
        instance = AuthControllers()
        email = "test@example.com"
        password = "invalid_password"

        mock_db_fetch_data.return_value = []

        result = instance.validate_user(email, password)

        assert not result

    def test_valdate_user__first_time_login(
        self,
        mock_db_fetch_data,
        mock_change_default_pwd,
        mock_employee_views,
        mock_hash_pwd,
    ):
        instance = AuthControllers()
        email = "test@example.com"
        password = "valid_password"

        mock_db_fetch_data.return_value = [
            (1, email, "hashed_password", "Admin", "False")
        ]

        result = instance.validate_user(email, password)

        mock_change_default_pwd.assert_called_once_with(email)

    @pytest.mark.parametrize("new_pwd, confirm_pwd", [("abc", "abc"), ("a123", "a123")])
    def test_change_default_pwd_positive(
        self, mocker, new_pwd, confirm_pwd, mock_hash_pwd, mock_db_save_data
    ):
        instance = AuthControllers()
        email = "test@example.com"

        mock_db_save_data.return_value = None

        mocker.patch(
            "controllers.auth_controllers.input_valid_password",
            side_effect=[new_pwd, confirm_pwd],
        )

        assert instance.change_default_pwd(email)

    @pytest.mark.parametrize("new_pwd, confirm_pwd", [("abcd", "abc")])
    def test_change_default_pwd_negative(
        self, mocker, new_pwd, confirm_pwd, mock_hash_pwd, mock_db_save_data
    ):
        instance = AuthControllers()
        email = "test@example.com"

        mock_db_save_data.return_value = None

        mocker.patch(
            "controllers.auth_controllers.input_valid_password",
            side_effect=[new_pwd, confirm_pwd],
        )
        with pytest.raises(StopIteration):
            instance.change_default_pwd(email)
