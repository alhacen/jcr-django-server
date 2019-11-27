from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse

from .models import Partner
from utils.classes import ExportCsvMixin


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ('name', 'code', 'seeker_registered')
    actions = ["export_as_csv"]
    exclude = ('seekers',)
    fields = (
        'seekers_details', 'code', 'name', 'city', 'pin_code',
        'state', 'address',
    )

    def seeker_registered(self, obj):
        return obj.seekers.count()

    def seekers_details(self, obj):
        seekers = ''
        for seeker in obj.seekers.all():
            seekers += f'<a href=\'{reverse("admin:seeker_seeker_change", args=(seeker.id,))}\'>{seeker}</a><br />'

        return format_html(seekers)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return 'code', 'seekers_details'

        return 'seekers_details',
