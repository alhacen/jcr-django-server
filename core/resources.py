from import_export import resources
from core.models import JobApplication


class JobApplicationResources(resources.ModelResource):
    class Meta:
        model = JobApplication
        fields = (
            'seeker__account__user__first_name', 'job__title__title',
            'job__organisation__name', 'seeker__account__phone',
            'answer', 'applied_on', 'status',

            'seeker__fathers_name', 'seeker__dob', 'seeker__gender', 'seeker__address', 'seeker__city',
            'seeker__pin_code', 'seeker__state',
            'seeker__educational_qualification', 'seeker__experience', 'seeker__aadhar',
            'seeker__job_title__title', 'seeker__account__phone', 'seeker__account__email',
            'seeker__account__alternate_phone', 'seeker__account__created_on',
        )
        export_order = fields
