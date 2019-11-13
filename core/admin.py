from django.contrib import admin
from django.utils.html import format_html

from core.models import Job, JobApplication, JobTitle
from utils.classes import ExportCsvMixin


admin.site.register(JobTitle)


@admin.register(Job)
class JobAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = (
        'organisation_name', 'title',
        'location', 'salary_range', 'min_experience',
        'status', 'applications'
    )
    list_display_links = ('organisation_name',)
    actions = ["export_as_csv"]

    def organisation_name(self, obj):
        return obj.organisation.name

    def applications(self, obj):
        return format_html(f'<a href="">{obj.jobapplication_set.count()}</a>')


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ('application', 'seeker_applied', 'job_applied_for', 'status', 'applied_on')
    list_display_links = ['application']
    actions = ["export_as_csv"]
    readonly_fields = ('seeker_applied', 'job_applied_for', 'applied_on')

    def application(self, obj):
        return 'View'

    def seeker_applied(self, obj):
        return format_html(
            f'<a href="/admin/seeker/seeker/{obj.seeker.id}/change/">{obj.seeker.name}</a>'
        )

    def job_applied_for(self, obj):
        return format_html(
            f'<a href="/admin/core/job/{obj.job.id}/change/">{obj.job}</a>'
        )
