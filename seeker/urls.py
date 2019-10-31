from django.urls import path

from .views import *


urlpatterns = [
    path('sign-up/', SeekerAPIView.as_view(), name='sign-up'),
    path('job/available/', JobAvailableAPIView.as_view(), name='job-available'),
    path('jobs/available/count/', count_job_view, name='job-available-count'),
    path('job/apply/', JobApplyAPIView.as_view(), name='job-applied'),
    path('job/apply/<int:job_id>/', JobApplyAPIView.as_view(), name='job-apply')
]

app_name = 'seeker'
