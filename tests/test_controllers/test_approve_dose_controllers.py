import pytest

from database.database_operations import db
from controllers.approve_dose_controllers import ApproveDoseControllers


@pytest.fixture
def instance(mocker):
    return ApproveDoseControllers()


class TestApproveDoseControllers:
    def test_show_info_to_approve(self, mocker, instance):
        mocker.patch(
            "controllers.approve_dose_controllers.db.fetch_data",
            return_value=[("sample data")],
        )
        assert instance.show_info_to_approve("") == [("sample data")]

    def test_approve_info(self, mocker, instance):
        mocker.patch("controllers.approve_dose_controllers.db.save_data")
        instance.approve_info(1)
        db.save_data.assert_called_once()
