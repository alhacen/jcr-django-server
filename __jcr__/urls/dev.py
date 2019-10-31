from django.urls import path, include
from __jcr__.secret import SECRET


urlpatterns = []

if SECRET['SERVER']['DEBUG'] and not SECRET['SERVER']['PRODUCTION']:
    urlpatterns = [
        path('', include('__jcr__.urls.api')),
        path('admin/', include('__jcr__.urls.admin')),
    ]
