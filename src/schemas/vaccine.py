from .schema_utils import CustomSchema
from marshmallow import Schema, fields, validate, validates_schema, ValidationError

class CreateVaccineSchema(CustomSchema):

    vaccine_name = fields.Str(required=True, validate=validate.Regexp("^[a-z,A-Z]+"))
    
class VaccineIdSchema(CustomSchema):

    vaccine_id = fields.Int(required=True)
