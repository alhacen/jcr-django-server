__all__ = ['Organisation', 'Employer']
from django.db import models
from django.utils.html import format_html

from seeker.validators import pin_code_validator
from utils.choices import STATE_CHOICES


class Employer(models.Model):
    account = models.OneToOneField('core.Account', on_delete=models.CASCADE)
    designation = models.CharField(max_length=255)

    def __str__(self):
        return format_html(
            f'{self.account.user.get_full_name()} ({self.designation} - {self.account.company}) '
            f'{self.account.phone} ({self.account.email})'
        )


class Organisation(models.Model):
    PROPRIETORSHIP = 'S'
    ONE_PERSON = 'O'
    SECTION_8 = '8'
    PARTNERSHIP = 'P'
    LIMITED_LIABILITY = 'L'
    PVT_LTD = 'C'
    PUBLIC_LTD = 'M'

    type_choices = (
        (PROPRIETORSHIP, 'Proprietorship'),
        (ONE_PERSON, 'One Person Company'),
        (SECTION_8, 'Section 8 Company'),
        (PARTNERSHIP, 'Partnership'),
        (LIMITED_LIABILITY, 'Limited Liability Partnership'),
        (PVT_LTD, 'Pvt. Ltd.'),
        (PUBLIC_LTD, 'Public Limited')
    )

    VERIFIED = 'V'
    PENDING = 'P'
    BLOCKED = 'B'

    status_choices = (
        (PENDING, 'Pending'),
        (VERIFIED, 'Verified'),
        (BLOCKED, 'Blocked')
    )

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=1, choices=type_choices)

    website = models.URLField(null=True, blank=True)
    phone = models.CharField(max_length=10)
    email = models.EmailField()

    address = models.TextField()
    city = models.CharField(max_length=255)
    pin_code = models.CharField(max_length=6, validators=[pin_code_validator])
    state = models.CharField(max_length=255, choices=STATE_CHOICES)

    employers = models.ManyToManyField('employer.Employer')
    root_employer = models.OneToOneField('employer.Employer', on_delete=models.PROTECT, related_name='root_employer')

    status = models.CharField(max_length=1, choices=status_choices)

    def __str__(self):
        return f'{self.name}'
