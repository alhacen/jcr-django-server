from django.urls import path, include


urlpatterns = [
    path('auth/', include('core.auth.urls', 'auth')),
]

app_name = 'core'
