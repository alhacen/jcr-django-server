from django.utils import timezone

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView

from core.models import JobTitle, Job
from utils.views import SignUpViewBase
from .models import Partner, PartnerUser
from seeker.serializers import SeekerSerializer
from seeker.models import Seeker


class PartnerAPIView(SignUpViewBase):
    account_type = 'P'

    def create_extra(self, request):
        """
        {
            organisation: {
                name: str,
                type: core.model.Organisation.type_choices,
                website: url,
                phone: str(10),
                address: text,
                pin_code: str(6),
                state: str,
                contact_person_name: str
            }
        }
        :param request:
        :return:
        """
        organisation = dict(request.data['partner'])
        self.user.first_name = organisation.pop('contact_person_name').title()
        self.user.save()

        root_user = PartnerUser.objects.create(
            account=self.account,
            designation=organisation.pop('contact_person_designation')
        )

        partner = Partner.objects.create(
            **organisation,
            root_user=root_user
        )

        partner.users.add(root_user)


@api_view(['GET'])
def count_job_view(request):
    titles = JobTitle.objects.filter()
    jobs_available = {}

    for title in titles:
        count = 0
        jobs = Job.objects.filter(
            title=title,
            status=Job.VERIFIED,
            apply_till__gte=timezone.now(),
        )
        for job in jobs:
            count += job.vacancies

        if count > 0:
            jobs_available[title.title] = count

    return Response(jobs_available)


@api_view(['GET'])
def get_code(request):
    return Response({
        'code': request.user.account.partner.code
    })


class GetMySeeker(ListAPIView):
    serializer_class = SeekerSerializer
    queryset = Partner.objects.all()

    def get_queryset(self):
        partner = self.request.user.account.partner
        self.queryset = partner.seekers.all()
        return super(GetMySeeker, self).get_queryset()
