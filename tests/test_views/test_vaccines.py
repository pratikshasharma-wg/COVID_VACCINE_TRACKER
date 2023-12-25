import pytest

from views.vaccines import VaccineViews


@pytest.fixture
def mock_vaccine_controller_class(mocker):
    return mocker.patch("views.vaccines.VaccineControllers")


class TestVaccineViews:
    def test_add_vaccine_positive(self, mocker, capsys, mock_vaccine_controller_class):
        mocker.patch("views.vaccines.add_valid_vaccine", return_value="vaccine")
        mock_vaccine_controller_class().create_vaccine.return_value = True
        VaccineViews().add_vaccine()
        captured = capsys.readouterr()
        assert "Vaccine Added Successfully!" in captured.out

    def test_add_vaccine_negative(self, mocker, mock_vaccine_controller_class, capsys):
        mocker.patch("views.vaccines.add_valid_vaccine", return_value="vaccine")
        mock_vaccine_controller_class().create_vaccine.return_value = False
        VaccineViews().add_vaccine()
        captured = capsys.readouterr()
        assert "Vaccine Already Exists!" in captured.out

    def test_view_vaccines_positive(self, mocker, mock_vaccine_controller_class):
        mock_vaccine_controller_class().show_vaccines.return_value = True
        mocker.patch("views.vaccines.display_table")
        vaccine_view_obj = VaccineViews()
        assert vaccine_view_obj.view_vaccines() is None

    def test_view_vaccines_negative(
        self, mocker, capsys, mock_vaccine_controller_class
    ):
        mock_vaccine_controller_class().show_vaccines.return_value = False
        vaccine_view_obj = VaccineViews()
        vaccine_view_obj.view_vaccines()
        captured = capsys.readouterr()
        assert "No Vaccine found!" in captured.out

    def test_get_vaccine_name_positive(self, mocker, mock_vaccine_controller_class):
        mocker.patch.object(VaccineViews, "view_vaccines")
        mocker.patch("builtins.input", return_value=1)
        mock_vaccine_controller_class().is_vaccine_present.return_value = True
        assert VaccineViews().get_vaccine_name()

    def test_get_vaccine_name_negative(
        self, mocker, mock_vaccine_controller_class, capsys
    ):
        mocker.patch.object(VaccineViews, "view_vaccines")
        mocker.patch("builtins.input", lambda a: 1)
        mock_vaccine_controller_obj = mock_vaccine_controller_class()
        mocker.patch.object(
            mock_vaccine_controller_obj, "is_vaccine_present", side_effect=[False, True]
        )
        captured = capsys.readouterr()
        result = VaccineViews().get_vaccine_name()
        if mock_vaccine_controller_obj.is_vaccine_present.return_value == False:
            assert "Please Enter valid Vaccine ID!" in captured.out
        assert result
