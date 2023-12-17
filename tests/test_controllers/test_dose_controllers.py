import pytest

from database.database_operations import db
from controllers.dose_controllers import DoseControllers

@pytest.fixture
def mock_db_fetch_data(mocker):
    return mocker.patch.object(db,'fetch_data', return_value = [("sample data")])

@pytest.fixture
def mock_db_save_data(mocker):
    return mocker.patch.object(db, 'save_data', return_value = None)

@pytest.fixture
def instance():
    return DoseControllers(1)

class TestDoseControllers:

    def test_fetch_dose_info(self, instance, mock_db_fetch_data):
        assert instance.fetch_dose_info() == [("sample data")]

    def test_fetch_vacc_status(self, instance, mock_db_fetch_data):
        assert instance.fetch_vacc_status() == [("sample data")]

    def test_add_dose_info(self, instance, mock_db_save_data):
        instance.add_dose_info('','','')
        db.save_data.assert_called()

    def test_update_dose_info(self, instance, mock_db_save_data):
        instance.update_dose_info('','','')
        db.save_data.assert_called()

    def test_fetch_approved_info(self, instance, mock_db_fetch_data):
        assert instance.fetch_approved_info() == [("sample data")]

    def test_check_id_present_positive(self, mock_db_fetch_data, instance):
        assert instance.check_id_present(1)

    def test_check_id_present_negative(self, instance, mocker):
        mocker.patch.object(db, 'fetch_data', return_value = None)
        assert not instance.check_id_present(1)