from django.contrib import admin
from django.urls import path
from django.shortcuts import reverse

from admin_auto_filters.filters import AutocompleteFilter
from import_export.admin import ExportActionModelAdmin

from .models import Seeker
from .resources import SeekerResources
from core.views import JobTitleSearchView


class JobTitleFilter(AutocompleteFilter):
    title = 'Job Types'
    field_name = 'job_title'

    def get_autocomplete_url(self, request, model_admin):
        return reverse('admin:seeker_custom_search')


class SeekerAdmin(ExportActionModelAdmin):
    date_hierarchy = 'account__created_on'

    resource_class = SeekerResources

    def mobile(self, instance):
        return instance.account.phone

    def created_on(self, instance):
        return instance.account.created_on

    list_filter = (
        JobTitleFilter,
    )

    search_fields = (
        'fathers_name', 'dob', 'gender',
        'address', 'city', 'pin_code', 'state',
        'educational_qualification', 'experience', 'aadhar',
        'job_title', 'account__phone'
    )

    list_display = (
        'name', 'fathers_name', 'gender',
        'dob', 'pin_code', 'mobile', 'aadhar', 'job_title', 'created_on'
    )

    readonly_fields = ('account',)
    fields = (
        'account', 'fathers_name', 'dob', 'gender',
        'address', 'city', 'pin_code', 'state',
        'educational_qualification', 'experience', 'aadhar',
        'job_title'
    )

    def has_add_permission(self, request):
        return False

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('seeker_custom_search/', self.admin_site.admin_view(JobTitleSearchView.as_view(model_admin=self)),
                 name='seeker_custom_search'),
        ]
        return custom_urls + urls


admin.site.register(Seeker, SeekerAdmin)
