import re
import pytest
from datetime import datetime, date

from utils import exceptions
from utils import input_validators
from database.database_operations import DBOperations



def test_input_valid_email_valid_email(mocker):
    mocker.patch("builtins.input", return_value="test@example.com")
    mocker.patch("src.utils.input_validators.db.fetch_data",lambda a, b: "")
    result = input_validators.input_valid_email()
    assert result == "test@example.com"


def test_input_valid_email_invalid_email(mocker, capsys):
    mock = mocker.patch("builtins.input", side_effect=["invalid-email", "example@gmail.com"])
    mocker.patch("src.utils.input_validators.db.fetch_data", lambda a, b: "")
    result = input_validators.input_valid_email()
    if mock.return_value == "invalid-email":
        captured = capsys.readouterr()
        assert "Enter valid input!" in captured.out
    assert result == "example@gmail.com"


def test_input_valid_email_existing_email(mocker, capsys):
    mocker.patch(
        "builtins.input", side_effect=["existing@example.com", "abc@gmail.com"]
    )
    mocker.patch(
        "src.utils.input_validators.db.fetch_data",
        side_effect =  ["existing@example.com", ""]
    )
    input_validators.input_valid_email()
    captured = capsys.readouterr()
    assert "Username already present!" in captured.out

def test_input_valid_password(mocker):
    mocker.patch('src.utils.input_validators.maskpass.askpass', lambda a: "123")
    mocker.patch.object(re,'fullmatch', side_effect = [None, True])
    assert input_validators.input_valid_password('') == "123"

def test_add_valid_vaccine_positive(mocker):
    mocker.patch('builtins.input', lambda a: "Vaccine")
    mocker.patch.object(re,'fullmatch', return_value = True)
    assert input_validators.add_valid_vaccine() == "vaccine"

def test_add_valid_vaccine_negative(mocker, capsys):
    mocker.patch('builtins.input', lambda a: "Vaccine")
    mocker.patch.object(re,'fullmatch', side_effect = [None, True])
    input_validators.add_valid_vaccine()
    captured = capsys.readouterr()
    assert "Enter valid vaccine name!" in captured.out
    
def test_input_name(mocker):
    mocker.patch('builtins.input', lambda a: "abc")
    mocker.patch.object(re, 'match', side_effect = [None, True])
    assert input_validators.input_name() == "abc"

def test_input_gender_valid(mocker):
    mocker.patch('builtins.input', lambda a: "male")
    return_val = input_validators.input_gender()
    assert return_val == "male"  

def test_input_gender_invalid(mocker, capsys):
    mocker.patch('builtins.input', side_effect = ["m", "male"])
    input_validators.input_gender()
    captured = capsys.readouterr()
    if input.return_value == "m":
        assert "Enter valid choice" in  captured.out  

def test_input_valid_date_invalid(mocker, capsys):
    mocker.patch('builtins.input', side_effect = ["hello", "12/12/2022"])
    return_val = input_validators.input_valid_date('')
    captured = capsys.readouterr()
    assert "Enter Valid date in dd/mm/yy format!" in captured.out

def test_input_valid_date_valid(mocker):
    mocker.patch('builtins.input', lambda a: "12/10/2022")
    return_val = input_validators.input_valid_date('')
    assert return_val == date('12/10/2022')

def test_input_valid_cid(mocker):
    mocker.patch('builtins.input', lambda a:"cid")
    mocker.patch.object(re, 'match', side_effect = [None, True])
    assert input_validators.input_valid_cid('') == "cid"

@pytest.mark.parametrize("inps,oups", [("1",True), ("2",False)])
def test_input_choice(mocker,inps, oups):
    mocker.patch('builtins.input', lambda a: inps)
    assert input_validators.input_choice('') == oups

def test_input_choice_invalid(mocker):
    mocker.patch('builtins.input', side_effect = ["3", "1"])
    assert input_validators.input_choice('') == True
