from marshmallow import Schema, fields

class AddDoseDetailsSchema(Schema):

    vaccine_name = fields.Str(required=True)
    dose_1_date = fields.Str(required=True)
    dose_1_cid = fields.Str(required=True)

class UpdateDoseDetailsSchema(Schema):

    dose_date = fields.Str(required=True)
    dose_cid = fields.Str(required=True)