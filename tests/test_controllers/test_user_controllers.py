import pytest

from controllers.user_controllers import UserControllers
from database.database_operations import db
from config.queries.db_queries import DbConfig

@pytest.fixture
def user_controllers_obj():
    return UserControllers()

class TestUserControllers:

    def test_create_user(self, mocker, capsys, user_controllers_obj):
        mocker.patch.object(db,'save_data')
        assert user_controllers_obj.create_user(1,'','') == None

    def test_update_name(self, mocker):
        mocker.patch.object(db,'save_data')
        assert UserControllers().update_name('', 1) == None

    def test_update_gender(self, mocker):
        mocker.patch('controllers.user_controllers.db.save_data')
        assert UserControllers().update_gender('',1) == None

    def test_show_all_users(self, mocker):
        mocker.patch('controllers.user_controllers.db.fetch_data', return_value = "1")
        assert UserControllers().show_all_users() == "1"


    @pytest.mark.parametrize("inp", [(0),(1),(2)])
    def test_show_users_by_dose(self,user_controllers_obj, inp, mocker):
        mocker.patch('controllers.user_controllers.db.fetch_data', return_value = "sample data")
        assert user_controllers_obj.show_users_by_dose(inp) == "sample data"

    @pytest.mark.parametrize("inp", [(1),(2)])
    def test_show_users_by_date(self,user_controllers_obj, inp, mocker):
        m = mocker.patch('controllers.user_controllers.db.fetch_data')
        m.return_value = "sample data"
        assert user_controllers_obj.show_users_by_date('',inp) == "sample data"

    def test_show_users_by_vaccine(self,user_controllers_obj, mocker):
        mocker.patch.object(db, 'fetch_data', return_value = "sample data")
        assert user_controllers_obj.show_users_by_vaccine('') == "sample data"