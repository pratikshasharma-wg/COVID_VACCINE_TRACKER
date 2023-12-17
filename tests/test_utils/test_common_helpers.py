import pytest
import builtins

from datetime import datetime,timedelta

from utils import common_helpers


def test_generate_uuid(mocker):
    # Test whether id of length = 4 is generated
    val = mocker.patch("shortuuid.ShortUUID.random", return_value="1234")
    common_helpers.generate_uuid()
    val.assert_called_once_with(4)

def test_check_date_diff_valid():
    # Test when the date difference is greater than 60 days
    date_1 = "01/01/2023"
    date_2 = "30/10/2022"
    assert common_helpers.check_date_diff(date_1, date_2) is True


def test_check_date_diff_invalid():
    # Test when the date difference is less than or equal to 60 days
    date_1 = "01/01/2023"
    date_2 = "05/11/2022"
    assert common_helpers.check_date_diff(date_1, date_2) is False


def test_check_date_diff_same_date():
    # Test when the dates are the same
    date_1 = "01/01/2023"
    date_2 = "01/01/2023"
    assert common_helpers.check_date_diff(date_1, date_2) is False

def test_is_future_date_future():
    # Test when the date is in the future
    future_date = (datetime.now() + timedelta(days=7)).strftime("%d/%m/%Y")
    assert common_helpers.is_future_date(future_date) is True


def test_is_future_date_today():
    # Test when the date is today
    today_date = (datetime.now()).strftime("%d/%m/%Y")
    assert common_helpers.is_future_date(today_date) is False


def test_is_future_date_past():
    # Test when the date is in the past
    past_date = (datetime.now() - timedelta(days=7)).strftime("%d/%m/%Y")
    assert common_helpers.is_future_date(past_date) is False

# def test_convert_to_datetime_obj():
#     date = "12/12/2022"
#     assert common_helpers.convert_to_datetime_obj(date) == date("12/12/2022")

def test_display_table(mocker, capsys):
    mocker.patch('utils.common_helpers.tabulate', return_value = "1")
    common_helpers.display_table([[1],[2]],["a","b"])
    captured = capsys.readouterr()
    assert "1" in captured.out