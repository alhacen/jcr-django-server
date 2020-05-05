from django.http.response import HttpResponse
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


def pong(request):
    return HttpResponse('pong')


urlpatterns = [
    path('ping/', pong),
    path('', include('core.urls', 'core')),
    path('seeker/', include('seeker.urls', 'seeker')),
    path('employer/', include('employer.urls', 'employer')),
    path('partner/', include('partner.urls', 'partner')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
