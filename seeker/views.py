__all__ = ['SeekerAPIView', 'JobAvailableAPIView', 'JobApplyAPIView', 'count_job_view']
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view

from utils.classes import FakeModel
from utils.views import SignUpViewBase
from utils.api import response

from core.models import Job, JobApplication, JobTitle
from partner.models import Partner
from core.serializers import JobSerializer, JobApplicationSerializer
from .models import Seeker


class SeekerAPIView(SignUpViewBase):
    seeker = FakeModel()
    account_type = 'S'

    def create_extra(self, request):
        """
        {
            seeker: {
                name: str,
                fathers_name: str,
                dob: DateTime,
                address: str,
                pin_code: str(6),
                state: state,
                educational_qualification: educational_qualification,
            }
        }
        :param request:
        :return:
        """

        seeker_data = dict(request.data['seeker'])
        self.user.first_name = seeker_data.pop('name').title()
        date = seeker_data.pop('dob')
        self.user.save()

        partner_code = seeker_data.pop('partner_code')

        partner = None
        if partner_code:
            partner = Partner.objects.get(code=partner_code)

        seeker = Seeker.objects.create(
            **seeker_data,
            job_title=JobTitle.objects.get(title=seeker_data.pop('job_title')),
            dob=date[:10],
            account=self.account,
        )

        if partner:
            partner.seekers.add(seeker)


class JobAvailableAPIView(ListAPIView):
    queryset = Job.objects.all().filter(
        status=Job.VERIFIED,
        apply_till__gte=timezone.now(),
    )
    serializer_class = JobSerializer

    def get_queryset(self):
        seeker = self.request.user.account.seeker
        if self.title_job == '':
            self.title_job = seeker.job_title

        self.queryset = self.queryset \
            .filter(
                title__title=self.title_job
            )\
            .exclude(
                jobapplication__seeker=seeker,
            )
        return super(JobAvailableAPIView, self).get_queryset()

    def get(self, request, *args, **kwargs):
        self.title_job = request.GET['title']
        return super(JobAvailableAPIView, self).get(request, *args, **kwargs)


class JobApplyAPIView(ListAPIView):
    serializer_class = JobApplicationSerializer

    def get_queryset(self):
        self.queryset = JobApplication.objects.filter(
            seeker=self.request.user.account.seeker
        ).order_by('-status_changed')
        return super(JobApplyAPIView, self).get_queryset()

    def post(self, request, job_id):
        seeker = request.user.account.seeker
        if not JobApplication.objects.filter(
                seeker=seeker,
                job_id=job_id
        ).exists():
            JobApplication.objects.create(
                seeker=seeker,
                job_id=job_id,
                status=JobApplication.APPLIED,
                answer=request.data['answer']
            )

        return response('Applied to the job')


@api_view(['GET'])
def count_job_view(request):
    titles = JobTitle.objects.filter()
    jobs_available = {}

    for title in titles:
        count = Job.objects.filter(
            title=title,
            status=Job.VERIFIED,
            apply_till__gte=timezone.now(),
        ).count()
        if count > 0:
            jobs_available[title.title] = count

    return Response(jobs_available)