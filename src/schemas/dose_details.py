from marshmallow import Schema, fields

class AddDoseDetailsSchema(Schema):

    vaccine_name = fields.Str(required=True)
    dose_date = fields.Str(required=True)
    dose_cid = fields.Str(required=True)
