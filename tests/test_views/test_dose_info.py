import pytest

from config.prints.prints import Prints
from views.dose_info import DoseInfoViews


@pytest.fixture
def obj_dose_info(mocker):
    mock = mocker.Mock()
    mocker.patch("views.dose_info.VaccineViews", return_value=mock)
    mocker.patch("views.dose_info.DoseControllers", return_value=mock)
    return DoseInfoViews(1)


class TestDoseInfoViews:
    def test_update_dose_info_already_updated(self, capsys, obj_dose_info):
        obj_dose_info.update_dose_info(3)
        captured = capsys.readouterr()
        assert Prints.STATUS_ALREADY_UPTODATE in captured.out

    @pytest.mark.parametrize("vacc_status", [(0), (1), (2)])
    def test_update_dose_info(self, mocker, vacc_status, obj_dose_info):
        mocker.patch.object(obj_dose_info, "update_dose_1_info")
        mocker.patch.object(obj_dose_info, "update_dose_2_info")
        return_val = obj_dose_info.update_dose_info(vacc_status)
        assert return_val is None

    def test_update_dose_1_info(self, mocker, obj_dose_info):
        obj_dose_info.vaccine_name = "vaccine"
        obj_dose_info.dose_1_date = "date"
        obj_dose_info.dose_1_cid = "cid"
        mocker.patch.object(obj_dose_info, "get_dose_1_info", return_value=True)
        mocker.patch.object(
            obj_dose_info.dose_controller_obj, "add_dose_info", lambda a, b, c: True
        )
        mocker.patch("views.dose_info.input_choice", lambda a: True)
        mocker.patch.object(obj_dose_info, "update_dose_2_info")
        return_val = obj_dose_info.update_dose_1_info()
        assert return_val is None

    def test_update_dose_2_info(self, mocker, obj_dose_info):
        obj_dose_info.dose_controller_obj.fetch_dose_info.return_value = [
            (1, 1, "vaccine_name", 1, "date")
        ]
        mocker.patch("views.dose_info.check_date_diff", lambda a, b: True)
        mocker.patch.object(obj_dose_info, "get_dose_2_info", return_value=True)
        obj_dose_info.dose_2_date = "date"
        obj_dose_info.dose_2_cid = "cid"
        mock = mocker.patch.object(
            obj_dose_info.dose_controller_obj, "update_dose_info"
        )
        obj_dose_info.update_dose_2_info()
        mock.assert_called_once()

    def test_update_dose_2_info_invalid(self, capsys, mocker, obj_dose_info):
        obj_dose_info.dose_controller_obj.fetch_dose_info.return_value = [
            (1, 1, "vaccine_name", 1, "date")
        ]
        mocker.patch("views.dose_info.check_date_diff", lambda a, b: False)
        obj_dose_info.update_dose_2_info()
        captured = capsys.readouterr()
        assert Prints.CANNOT_UPDATE_DOSE2 in captured.out

    def test_get_dose_1_info(self, mocker, obj_dose_info):
        obj_dose_info.vaccine_obj.get_vaccine_name.return_value = "vaccine"
        mocker.patch("views.dose_info.input_valid_date", lambda a: "date")
        mocker.patch("views.dose_info.is_future_date", lambda a: False)
        mocker.patch("views.dose_info.input_valid_cid", lambda a: "cid")
        mocker.patch.object(obj_dose_info, "is_acceptable_id", lambda a: True)
        mocker.patch("views.dose_info.input_choice", return_value=True)
        assert obj_dose_info.get_dose_1_info() is True

    def test_get_dose_1_info_future_date(self, capsys, mocker, obj_dose_info):
        obj_dose_info.dose_1_date = "date"
        mocker.patch("views.dose_info.input_valid_date", lambda a: "date")
        mocker.patch("views.dose_info.is_future_date", side_effect=[True, False])
        mocker.patch("views.dose_info.input_valid_cid", lambda a: "cid")
        mocker.patch.object(obj_dose_info, "is_acceptable_id", lambda a: True)
        mocker.patch("views.dose_info.input_choice", return_value=True)
        obj_dose_info.get_dose_1_info()
        captured = capsys.readouterr()
        assert Prints.FUTURE_DATE_MSG in captured.out

    def test_get_dose_1_info_date_cid_exists(self, capsys, mocker, obj_dose_info):
        obj_dose_info.dose_1_date = "date"
        mocker.patch("views.dose_info.input_valid_date", lambda a: "date")
        mocker.patch("views.dose_info.is_future_date", lambda a: False)
        mocker.patch("views.dose_info.input_valid_cid", lambda a: "cid")
        mocker.patch.object(
            obj_dose_info, "is_acceptable_id", side_effect=[False, True]
        )
        mocker.patch("views.dose_info.input_choice", return_value=True)
        obj_dose_info.get_dose_1_info()
        captured = capsys.readouterr()
        assert "Enter Valid CID!" in captured.out

    def test_get_dose_2_info(self, capsys, mocker, obj_dose_info):
        obj_dose_info.dose_1_date = "date"
        mocker.patch("views.dose_info.input_valid_date", lambda a: "date")
        mocker.patch("views.dose_info.is_future_date", lambda a: False)
        mocker.patch("views.dose_info.check_date_diff", lambda a, b: True)
        mocker.patch("views.dose_info.input_valid_cid", lambda a: "cid")
        mocker.patch.object(obj_dose_info, "is_acceptable_id", lambda a: True)
        mocker.patch("views.dose_info.input_choice", return_value=True)
        assert obj_dose_info.get_dose_2_info() is True

    def test_get_dose_2_info_future_date(self, capsys, mocker, obj_dose_info):
        obj_dose_info.dose_1_date = "date"
        mocker.patch("views.dose_info.input_valid_date", lambda a: "date")

        mocker.patch("views.dose_info.is_future_date", side_effect=[True, False])
        mocker.patch("views.dose_info.check_date_diff", lambda a, b: True)
        mocker.patch("views.dose_info.input_valid_cid", lambda a: "cid")
        mocker.patch.object(obj_dose_info, "is_acceptable_id", lambda a: True)
        mocker.patch("views.dose_info.input_choice", return_value=True)
        obj_dose_info.get_dose_2_info()
        captured = capsys.readouterr()
        assert Prints.FUTURE_DATE_MSG in captured.out

    def test_get_dose_2_info_date_diff_not_60(self, capsys, mocker, obj_dose_info):
        obj_dose_info.dose_1_date = "date"
        mocker.patch("views.dose_info.input_valid_date", lambda a: "date")
        mocker.patch("views.dose_info.is_future_date", lambda a: False)
        mocker.patch("views.dose_info.check_date_diff", side_effect=[False, True])
        mocker.patch("views.dose_info.input_valid_cid", lambda a: "cid")
        mocker.patch.object(obj_dose_info, "is_acceptable_id", lambda a: True)
        mocker.patch("views.dose_info.input_choice", return_value=True)
        obj_dose_info.get_dose_2_info()
        captured = capsys.readouterr()
        assert Prints.DOSE2_DATE_INVALID in captured.out

    def test_get_dose_2_info_date_cid_exists(self, capsys, mocker, obj_dose_info):
        obj_dose_info.dose_1_date = "date"
        mocker.patch("views.dose_info.input_valid_date", lambda a: "date")
        mocker.patch("views.dose_info.is_future_date", lambda a: False)
        mocker.patch("views.dose_info.check_date_diff", lambda a, b: True)
        mocker.patch("views.dose_info.input_valid_cid", lambda a: "cid")
        mocker.patch.object(
            obj_dose_info, "is_acceptable_id", side_effect=[False, True]
        )
        mocker.patch("views.dose_info.input_choice", return_value=True)
        obj_dose_info.get_dose_2_info()
        captured = capsys.readouterr()
        assert "Enter Valid CID!" in captured.out

    @pytest.mark.parametrize("input, return_val", [(True, False), (False, True)])
    def test_is_acceptable_id(self, input, return_val, obj_dose_info, mocker):
        obj_dose_info.dose_controller_obj.check_id_present.return_value = input
        assert obj_dose_info.is_acceptable_id(1) is return_val