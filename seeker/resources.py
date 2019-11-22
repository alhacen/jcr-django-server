from import_export import resources
from seeker.models import Seeker


class SeekerResources(resources.ModelResource):
    class Meta:
        model = Seeker
        fields = (
            'account__user__first_name', 'fathers_name', 'dob', 'gender', 'address', 'city', 'pin_code', 'state',
            'educational_qualification', 'experience', 'aadhar', 'job_title__title', 'account__phone', 'account__email',
            'account__alternate_phone', 'account__created_on',
        )
        export_order = fields
