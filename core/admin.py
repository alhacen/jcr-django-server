from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse

from import_export.admin import ExportActionModelAdmin
from core.models import Job, JobApplication, JobTitle
from utils.classes import ExportCsvMixin
from core.resources import JobApplicationResources


@admin.register(JobTitle)
class JobTitleAdmin(admin.ModelAdmin):
    search_fields = ['title']


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
        return format_html(f'<a href=\'{reverse("admin:core_jobapplication_changelist")}\'>{obj.jobapplication_set.count()}</a>')


@admin.register(JobApplication)
class JobApplicationAdmin(ExportActionModelAdmin):
    list_display = ('application', 'seeker_applied', 'job_applied_for', 'status', 'applied_on')
    list_display_links = ['application']
    readonly_fields = ('seeker_applied', 'job_applied_for', 'applied_on')
    resource_class = JobApplicationResources

    def application(self, obj):
        return 'View'

    def seeker_applied(self, obj):
        return format_html(
            f'<a href=\'{reverse("admin:seeker_seeker_change", args=(obj.seeker.id,))}\'>{obj.seeker.name}</a>'
        )

    def job_applied_for(self, obj):
        return format_html(
            f'<a href=\'{reverse("admin:core_job_change", args=(obj.job.id,))}\'>{obj.job}</a>'
        )

    def has_add_permission(self, request):
        return False
