from marshmallow import fields, validate, validates
from datetime import datetime

from schemas.schema_utils import CustomSchema
from utils.exceptions import FailedValidation

class AddDoseDetailsSchema(CustomSchema):

    vaccine_name = fields.Str(required=True)
    dose_date = fields.Date(format='%d/%m/%Y', required=True)
    dose_cid = fields.String(required=True, validate=validate.Regexp(r'^[a-zA-Z0-9]{1,8}$'))

    @validates('dose_date')
    def validate_dose_date(self, dose_date):
        current_date = datetime.now().date()
        if dose_date > current_date:
            raise FailedValidation(422, 'Unprocessable Entity', 'Only dates till now can be selected.')
