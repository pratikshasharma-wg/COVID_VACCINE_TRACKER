from marshmallow import fields, ValidationError, validates
from datetime import datetime

from schemas.schema_utils import CustomSchema
from utils.exceptions import FailedValidation

class AddDoseDetailsSchema(CustomSchema):

    vaccine_name = fields.Str(required=True)
    dose_date = fields.Date(format='%d/%m/%Y', required=True)
    dose_cid = fields.Str(required=True)

    @validates('dose_date')
    def validate_dose_date(self, dose_date):
        current_date = datetime.now().date()
        if dose_date > current_date:
            raise FailedValidation(422, 'Unprocessable Entity', 'Only dates till now can be selected.')
