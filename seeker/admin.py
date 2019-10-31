from django.contrib import admin
from .models import Seeker

from utils.classes import ExportCsvMixin


@admin.register(Seeker)
class SeekerAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = (
        'name', 'fathers_name', 'gender',
        'dob', 'pin_code', 'aadhar', 'job_title'
    )
    readonly_fields = ('account',)
    fields = (
        'account', 'fathers_name', 'dob', 'gender',
        'address', 'city', 'pin_code', 'state',
        'educational_qualification', 'experience', 'aadhar',
        'job_title'
    )
    actions = ["export_as_csv"]
