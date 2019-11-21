from django.contrib import admin
from .models import Seeker
from admin_auto_filters.filters import AutocompleteFilter
from import_export.admin import ExportActionModelAdmin
from .resources import SeekerResources

"""
class GenderFilter(AutocompleteFilter):
    title = 'Gender'
    field_name = Seeker.gender
    class Meta:
        pass
"""
class SeekerAdmin(ExportActionModelAdmin):
    #search_fields = ['gender']
    #list_filter = [GenderFilter]
    date_hierarchy = 'account__created_on'

    resource_class = SeekerResources

    def mobile(self, instance):
        return instance.account.phone

    def created_on(self, instance):
        return instance.account.created_on

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

    #class Media:
     #   pass


admin.site.register(Seeker, SeekerAdmin)
