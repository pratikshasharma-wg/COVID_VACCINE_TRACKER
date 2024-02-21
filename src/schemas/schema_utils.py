from typing import Any
from utils.exceptions import FailedValidation
from marshmallow import Schema, ValidationError

class CustomSchema(Schema):
    def handle_error(self, error: ValidationError, data: Any, *, many: bool, **kwargs):
        raise FailedValidation(422, "Unprocessible Entity", error.messages)
