from marshmallow import fields
from .schema_utils import CustomSchema

class AddDoseDetailsSchema(CustomSchema):

    vaccine_name = fields.Str(required=True)
    dose_date = fields.Str(required=True)
    dose_cid = fields.Str(required=True)
