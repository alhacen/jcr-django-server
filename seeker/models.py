__all__ = ['Seeker']
from django.db import models

from utils.choices import STATE_CHOICES, EDUCATIONAL_QUALIFICATION_CHOICES, ExperienceChoices, GenderChoice
from .validators import pin_code_validator


class Seeker(models.Model):
    account = models.OneToOneField('core.Account', on_delete=models.CASCADE)

    fathers_name = models.CharField(max_length=49)
    dob = models.DateField()
    gender = models.CharField(max_length=1, choices=GenderChoice.choices)

    address = models.TextField()
    city = models.CharField(max_length=255)
    pin_code = models.CharField(max_length=6, validators=[pin_code_validator])
    state = models.CharField(choices=STATE_CHOICES, max_length=255)

    educational_qualification = models.CharField(max_length=255, choices=EDUCATIONAL_QUALIFICATION_CHOICES)
    experience = models.IntegerField(choices=ExperienceChoices.choices)

    aadhar = models.CharField(max_length=12)
    job_title = models.ForeignKey('core.JobTitle', on_delete=models.DO_NOTHING)

    @property
    def name(self):
        return self.account.user.get_full_name()

    def save(self, **kwargs):
        self.full_clean()
        super(Seeker, self).save(**kwargs)

    def __str__(self):
        return f'{self.account.user.get_full_name()} S/o {self.fathers_name} [Aadhar: {self.aadhar}]'
