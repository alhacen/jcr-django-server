from django.urls import path
from .views import PartnerAPIView, count_job_view, get_code, GetMySeeker

urlpatterns = [
    path('sign-up/', PartnerAPIView.as_view(), name='sign-up'),
    path('jobs/', count_job_view, name='count-jobs'),
    path('code/', get_code, name='get-code'),
    path('seeker/', GetMySeeker.as_view(), name='seekers')
]

app_name = 'partner'
