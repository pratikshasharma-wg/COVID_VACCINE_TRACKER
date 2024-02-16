from marshmallow import Schema, fields

class LoginUserSchema(Schema):

    email = fields.Str(required=True)
    password = fields.Str(required=True)

