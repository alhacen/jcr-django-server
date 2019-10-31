from django.db import models

from utils.crypto import generate_hash
from django.utils.html import format_html
from utils.choices import STATE_CHOICES


class PartnerUser(models.Model):
    account = models.OneToOneField('core.Account', on_delete=models.CASCADE)
    designation = models.CharField(max_length=255)

    def __str__(self):
        return format_html(
            f'{self.account.user.get_full_name()} ({self.designation} - {self.account.company}) '
            f'{self.account.phone} ({self.account.email})'
        )


class Partner(models.Model):
    name = models.CharField(max_length=255)

    city = models.CharField(max_length=255)
    pin_code = models.CharField(max_length=6)
    state = models.CharField(choices=STATE_CHOICES, default="National Capital Territory of Delhi", max_length=255)
    address = models.TextField()

    verified = models.BooleanField(default=False)
    code = models.CharField(max_length=6, unique=True)
    seekers = models.ManyToManyField('seeker.Seeker')

    root_user = models.OneToOneField(PartnerUser, on_delete=models.CASCADE, related_name='root_user')
    users = models.ManyToManyField(PartnerUser)

    def save(self, *args, **kwargs):
        if self.code:
            self.code = self.code.lower().replace(' ', '')
        else:
            self.code = generate_hash('sha256', self.name)[:6].lower()

        super(Partner, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} - {self.code}'
