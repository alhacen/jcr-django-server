from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('', admin.site.urls),
]

admin.site.site_header = "Just Clean Rojgar Administration"
admin.site.site_title = "Just Clean Rojgar Admin Portal"
admin.site.index_title = "Just Clean Rojgar"
