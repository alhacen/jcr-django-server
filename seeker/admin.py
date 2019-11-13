from django.contrib import admin
from .models import Seeker
from core.auth.models import Account
from utils.classes import ExportCsvMixin
from import_export.admin import ImportExportModelAdmin


@admin.register(Seeker)
class SeekerAdmin(ImportExportModelAdmin):

    def mobile(self, instance):
        return instance.account.phone

    list_display = (
        'name', 'fathers_name', 'gender',
        'dob', 'pin_code', 'mobile', 'aadhar', 'job_title'
    )

    readonly_fields = ('account',)
    fields = (
        'account', 'fathers_name', 'dob', 'gender',
        'address', 'city', 'pin_code', 'state',
        'educational_qualification', 'experience', 'aadhar',
        'job_title'
    )


