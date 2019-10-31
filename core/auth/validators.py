__all__ = ['phone_number_validator']
from django.core.exceptions import ValidationError


def phone_number_validator(value):
    """
    Checks validity of indian phone number

    :param value: Indian Phone number a 10 digit integer
    :return: None
    """
    if len(value) != 10:
        raise ValidationError('Phone number should be of 10 digit')
    try:
        int(value)
    except ValueError:
        raise ValidationError('Phone number is not valid')
