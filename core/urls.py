from django.urls import path, include
from .views import JobListViews


urlpatterns = [
    path('auth/', include('core.auth.urls', 'auth')),
    path('job-titles/', JobListViews.as_view(), name='job-title')
]

app_name = 'core'
