from django.contrib import admin
from django.utils.html import format_html
from import_export.admin import ExportActionModelAdmin
from .models import Organisation, Employer
from utils.classes import ExportCsvMixin


@admin.register(Employer)
class EmployerAdmin(ExportActionModelAdmin):
    list_display = ('name', 'company', 'designation', 'phone', 'email')
    fields = ('account', 'designation')
    readonly_fields = ('account',)

    def name(self, obj):
        return obj.account.user.get_full_name()

    def company(self, obj):
        return format_html(
            f'<a href="/admin/employer/organisation/{obj.account.company.id}/change/">{obj.account.company}</a>')

    def phone(self, obj):
        return obj.account.phone

    def email(self, obj):
        return obj.account.email

    def has_add_permission(self, request):
        return False


@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ('name', 'type', 'website', 'phone', 'main_employer')
    readonly_fields = ('root_employer',)
    exclude = ('employers',)
    actions = ["export_as_csv"]

    def main_employer(self, obj):
        return format_html(
            f'<a href="/admin/employer/employer/{obj.root_employer.id}/change/">{obj.root_employer.account}</a>'
        )
