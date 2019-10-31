from django.urls import path
from .views import *


urlpatterns = [
    path('sign-up/', EmployerAPIView.as_view(), name='sign-up'),
    path('jobs/', JobAPIView.as_view(), name='post-job'),
    path('jobs/seekers/', count_seeker_view, name='seeker-available'),
    path('jobs/<int:job_id>/', JobSeekerAPIView.as_view(), name='job-seekers'),
    path('jobs/<int:job_id>/', JobSeekerAPIView.as_view(), name='job-seekers-status-change')
]

app_name = 'employer'
