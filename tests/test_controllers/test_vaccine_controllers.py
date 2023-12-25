import pytest

from database.database_operations import db
from controllers.vaccine_controllers import VaccineControllers


class TestVaccineControllers:
    @pytest.mark.parametrize("inp, out", [("abc", False), ("", True)])
    def test_create_vaccine(self, mocker, inp, out):
        mocker.patch.object(db, "fetch_data", return_value=inp)
        mocker.patch.object(db, "save_data")
        assert VaccineControllers().create_vaccine("") == out

    def test_show_vaccines(self, mocker):
        mock_data = mocker.patch(
            "src.controllers.vaccine_controllers.db.fetch_data", return_value="abc"
        )
        assert VaccineControllers.show_vaccines() == "abc"

    def test_is_vaccine_present_positive(self, mocker):
        mocker.patch.object(db, "fetch_data", return_value=[(1, "Vaccine name")])
        assert VaccineControllers().is_vaccine_present(1)

    def test_is_vaccine_present_negative(self, mocker):
        mocker.patch.object(db, "fetch_data", return_value=[])
        assert VaccineControllers().is_vaccine_present(1) == False
