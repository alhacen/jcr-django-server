from django.contrib import admin

from .models import Partner
from utils.classes import ExportCsvMixin


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ('name', 'code', 'seeker_registered')
    actions = ["export_as_csv"]

    def seeker_registered(self, obj):
        return obj.seekers.count()

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return 'code', 'seekers'

        return 'seekers',
