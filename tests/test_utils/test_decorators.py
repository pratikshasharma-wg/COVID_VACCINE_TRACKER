import pytest

from src.config.logs.logs import Logs
from src.config.prints.prints import Prints
from src.config.prompts.prompts import PromptsConfig
from src.config.queries.db_queries import DbConfig
from src.utils.decorators import load_config


def test_load_config(mocker):
    # Mock the load methods
    mocker.patch.object(DbConfig, "load")
    mocker.patch.object(PromptsConfig, "load")
    mocker.patch.object(Prints, "load")
    mocker.patch.object(Logs, "load")

    func_called = False

    def mock_func():
        nonlocal func_called
        func_called = True

    decorated_func = load_config(mock_func)
    decorated_func()

    assert func_called
