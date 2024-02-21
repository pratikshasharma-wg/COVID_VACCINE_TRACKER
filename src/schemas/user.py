from .schema_utils import CustomSchema
from marshmallow import Schema, fields, validate, validates_schema, ValidationError

class AddUserSchema(CustomSchema):

    email = fields.Str(required=True, validate=validate.Regexp("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,7}$"))
    password = fields.Str(required=True, validate=validate.Regexp("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"))

class UpdatePersonalDetailsSchema(CustomSchema):

    name = fields.Str(required=True, validate=validate.Regexp("^[a-z,A-Z ]{1,20}$"))
    gender = fields.Str(required=True, validate=validate.Regexp("male" or "female"))
