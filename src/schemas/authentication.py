from marshmallow import Schema, fields
from .schema_utils import CustomSchema

class LoginUserSchema(CustomSchema):

    email = fields.Str(required=True)
    password = fields.Str(required=True)

