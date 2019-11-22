from import_export import resources
from core.models import JobApplication


class JobApplicationResources(resources.ModelResource):
    class Meta:
        model = JobApplication
        fields = (
            'seeker__account__user__first_name', 'job__title__title',
            'job__organisation__name', 'seeker__account__phone',
            'answer', 'applied_on', 'status'
        )
        export_order = fields
