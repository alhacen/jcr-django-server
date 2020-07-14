__all__ = ['Account']

from django.db import models
from django.core.exceptions import ValidationError

from .validators import phone_number_validator


class Account(models.Model):
    EMPLOYER = 'E'
    SEEKER = 'S'
    PARTNER = 'P'
    OTHERS = 'O'

    USER_TYPE = (
        (EMPLOYER, 'Employer'),
        (SEEKER, 'Seeker'),
        (PARTNER, 'Partner'),
        (OTHERS, 'Others')
    )

    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=USER_TYPE)

    phone = models.CharField(max_length=10, validators=[phone_number_validator], unique=True)
    email = models.EmailField(null=True, blank=True, unique=True)
    alternate_phone = models.CharField(max_length=10, validators=[phone_number_validator], null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    otp = models.TextField(null=True, blank=True)

    @property
    def is_employer(self):
        return self.type == Account.EMPLOYER

    @property
    def is_seeker(self):
        return self.type == Account.SEEKER

    @property
    def is_partner(self):
        return self.type == Account.PARTNER

    @property
    def company(self):
        try:
            return self.employer.organisation_set.all()[0]
        except (KeyError, AttributeError):
            return None

    @property
    def partner(self):
        try:
            return self.partneruser.partner_set.all()[0]
        except (KeyError, AttributeError):
            return None

    def full_clean(self, exclude=None, validate_unique=True):
        super(Account, self).full_clean(exclude=None, validate_unique=True)
        if self.type == Account.EMPLOYER and not self.email:
            raise ValidationError('Email is required for Employer')

    def account_type(self):
        if self.is_seeker:
            self.seeker
        elif self.is_employer:
            self.employer
        elif self.is_partner:
            self.partner
        else:
            raise Exception('Invalid login')

        return self.type

    def save(self, **kwargs):
        self.full_clean()
        super(Account, self).save(**kwargs)

    def __str__(self):
        return f'{self.user.get_full_name()} [ Phone: {self.phone}, Email: {self.email} ]'
