from django.db import models
from .auth.models import *
from utils.choices import ExperienceChoices, GenderChoice, EDUCATIONAL_QUALIFICATION_CHOICES


class JobTitle(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Job(models.Model):
    VERIFIED = 'V'
    PENDING = 'P'
    NOT_VERIFIED = 'B'

    status_choices = (
        (PENDING, 'Pending'),
        (VERIFIED, 'Verified'),
        (NOT_VERIFIED, 'Not Verified')
    )

    organisation = models.ForeignKey('employer.Organisation', on_delete=models.CASCADE)

    title = models.ForeignKey(JobTitle, on_delete=models.DO_NOTHING)
    vacancies = models.IntegerField()
    min_experience = models.IntegerField(choices=ExperienceChoices.choices)

    location = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GenderChoice.choices, null=True, blank=True)

    educational_qualification = models.CharField(max_length=255, choices=EDUCATIONAL_QUALIFICATION_CHOICES)

    salary_range = models.CharField(max_length=255, null=True, blank=True)
    salary_range_in_hand = models.CharField(max_length=255, null=True, blank=True)

    status = models.CharField(max_length=1, choices=status_choices)

    questions = models.TextField(null=True, blank=True)
    eligibility = models.TextField(null=True, blank=True)
    additional_info = models.TextField(null=True, blank=True)

    reporting_location = models.TextField()

    posted = models.DateTimeField(auto_now_add=True)
    apply_till = models.DateField()

    def __str__(self):
        return f'{self.organisation} -> {self.title} [{self.status}]'


class JobApplication(models.Model):
    APPLIED = 'A'
    SEEN = 'S'
    SELECTED = 'D'
    REJECTED = 'R'
    JOINED = 'J'
    BLACKLISTED = 'B'

    status_choices = (
        (APPLIED, 'Pending'),
        (SEEN, 'Seen'),
        (SELECTED, 'Selected'),
        (REJECTED, 'Rejected'),
        (JOINED, 'Joined'),
        (BLACKLISTED, 'Blacklisted')
    )

    job = models.ForeignKey('core.Job', on_delete=models.CASCADE)
    seeker = models.ForeignKey('seeker.Seeker', on_delete=models.CASCADE)

    status = models.CharField(max_length=1, choices=status_choices)
    answer = models.TextField(null=True, blank=True)

    applied_on = models.DateTimeField(auto_now_add=True)
    status_changed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.seeker.account.user.get_full_name()} -> {self.job}'
