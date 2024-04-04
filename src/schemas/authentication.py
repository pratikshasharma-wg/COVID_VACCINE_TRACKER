from marshmallow import fields
from .schema_utils import CustomSchema


class LoginUserSchema(CustomSchema):

    email = fields.Str(required=True)
    password = fields.Str(required=True)


class ChangePasswordSchema(CustomSchema):

    old_password = fields.Str()
    new_password = fields.Str(required=True)
