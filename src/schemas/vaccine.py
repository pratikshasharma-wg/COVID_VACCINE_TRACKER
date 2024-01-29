from marshmallow import Schema, fields, validate, validates_schema, ValidationError

class CreateVaccineSchema(Schema):

    vaccine_name = fields.Str(required=True, validate=validate.Regexp("^[a-z,A-Z]+"))
    