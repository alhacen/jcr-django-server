from django.core.exceptions import ValidationError


def pin_code_validator(value):
    if not len(value) == 6:
        raise ValidationError('Pin code not valid')
