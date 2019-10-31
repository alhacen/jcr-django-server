__all__ = [
    'EmployerAPIView', 'JobAPIView',
    'JobSeekerAPIView', 'count_seeker_view'
]
from django.utils.timezone import datetime

from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from core.models import Job, JobApplication
from core.serializers import JobSerializer
from seeker.serializers import SeekerSerializer
from seeker.models import Seeker
from utils.views import SignUpViewBase
from utils.api import response
from .models import Organisation, Employer
from core.models import JobTitle


class EmployerAPIView(SignUpViewBase):
    account_type = 'E'

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
        organisation = dict(request.data['organisation'])
        self.user.first_name = organisation.pop('contact_person_name').title()
        self.user.save()

        root_user = Employer.objects.create(
            account=self.account,
            designation=organisation.pop('contact_person_designation')
        )

        organisation = Organisation.objects.create(
            **organisation,
            status=Organisation.PENDING,
            root_employer=root_user
        )

        organisation.employers.add(root_user)


class JobAPIView(ListAPIView):
    serializer_class = JobSerializer

    def get_queryset(self):
        self.queryset = Job.objects.filter(
            organisation=self.request.user.account.company
        )
        return super(JobAPIView, self).get_queryset()

    def post(self, request):
        data = dict(request.data)
        date = data.pop('apply_till')[:10]
        title = JobTitle.objects.get(title=data.pop('title'))

        Job.objects.create(
            **data,
            title=title,
            apply_till=date,
            organisation=request.user.account.company,
            status=Job.PENDING,
        )
        return response('Job added')


class JobSeekerAPIView(ListAPIView):
    serializer_class = SeekerSerializer

    def get_queryset(self):
        _ = self.request.user.account.company
        self.queryset = Seeker.objects.filter(
            jobapplication__job_id=self.job_id
        )
        return super(JobSeekerAPIView, self).get_queryset()

    def get(self, request, *args, **kwargs):
        self.job_id = kwargs.pop('job_id')
        if not Job.objects.filter(id=self.job_id, status=Job.VERIFIED).exists():
            return Response([])

        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True, job_id=self.job_id)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True, job_id=self.job_id)
        return Response(serializer.data)

    def post(self, request, job_id):
        new_status = request.data['status']
        JobApplication.objects.filter(
            seeker_id__in=request.data['seekers'],
            job_id=job_id,
        ).update(status=new_status, status_changed=datetime.now())
        return response('Changed status')


@api_view(['GET'])
def count_seeker_view(request):
    titles = JobTitle.objects.filter()
    seekers_available = {}

    for title in titles:
        count = Seeker.objects.filter(job_title=title).count()
        if count > 0:
            seekers_available[title.title] = count

    return Response(seekers_available)
