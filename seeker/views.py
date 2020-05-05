__all__ = ['SeekerAPIView', 'JobAvailableAPIView', 'JobApplyAPIView', 'count_job_view', 'DocsListView']

from datetime import datetime

from django.db.models import Q
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view

from utils.classes import FakeModel
from utils.views import SignUpViewBase
from utils.api import response

from core.models import Job, JobApplication, JobTitle, Account
from employer.models import Organisation
from partner.models import Partner
from core.serializers import JobSerializer, JobApplicationSerializer
from .models import Seeker, SeekerDocuments
from .serializers import SeekerDocumentsSerializer


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
        date = datetime.strptime(date, '%d-%m-%Y')
        print(date, '-' * 50)

        self.user.set_password(f'{str(date.day).rjust(2, "0")}{str(date.month).rjust(2, "0")}')
        self.user.save()

        partner_code = seeker_data.pop('partner_code')

        partner = None
        if partner_code:
            partner = Partner.objects.get(code=partner_code)

        seeker = Seeker.objects.create(
            **seeker_data,
            job_title=JobTitle.objects.get(title=seeker_data.pop('job_title')),
            dob=date,
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
            .filter(title__title=self.title_job) \
            .exclude(jobapplication__seeker=seeker, )
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


class DocsListView(ListAPIView):
    queryset = SeekerDocuments.objects.all()
    serializer_class = SeekerDocumentsSerializer

    def get_queryset(self):
        user = self.request.user
        seeker = user.account.seeker

        docs_job_title = JobTitle.objects.filter(id=seeker.job_title_id)
        docs_job = seeker.jobapplication_set.all()
        docs_org = Organisation.objects.filter(job__jobapplication__seeker=seeker)
        docs_partner = Partner.objects.filter(seekers__account=user.account)

        return SeekerDocuments.objects.filter(
            Q(job_title__in=docs_job_title) |
            Q(job__jobapplication__in=docs_job) |
            Q(organisation__in=docs_org) |
            Q(partner__in=docs_partner) |
            Q(seeker=seeker)
        )
