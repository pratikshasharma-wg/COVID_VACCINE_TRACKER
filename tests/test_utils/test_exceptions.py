import pytest

from utils.exceptions import (
    UsernameAlreadyExistsError,
    DoseInfoNotFoundError,
    CIDAlreadyExistsError,
    EmptyNameError,
    VaccineNameError,
    ValidNameError,
)


def test_username_already_exists_error():
    with pytest.raises(
        UsernameAlreadyExistsError, match="Username already exists: test_user"
    ):
        raise UsernameAlreadyExistsError("Username already exists: test_user")
    assert UsernameAlreadyExistsError("Username already exists: test_user").msg == "Username already exists: test_user"
    

def test_username_already_exists_error_msg():
    error_msg = "error msg"
    obj = UsernameAlreadyExistsError(error_msg)
    assert obj.msg == error_msg


def test_dose_info_not_found_error():
    with pytest.raises(DoseInfoNotFoundError):
        raise DoseInfoNotFoundError()


def test_cid_already_exists_error():
    with pytest.raises(CIDAlreadyExistsError, match="CID already exists: test_cid"):
        raise CIDAlreadyExistsError("CID already exists: test_cid")


def test_empty_name_error():
    with pytest.raises(EmptyNameError, match="Name cannot be empty"):
        raise EmptyNameError("Name cannot be empty")


def test_vaccine_name_error():
    with pytest.raises(VaccineNameError, match="Invalid vaccine name: test_vaccine"):
        raise VaccineNameError("Invalid vaccine name: test_vaccine")


def test_valid_name_error():
    with pytest.raises(ValidNameError, match="Invalid name: test_name"):
        raise ValidNameError("Invalid name: test_name")