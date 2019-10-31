from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('', admin.site.urls),
]

admin.site.site_header = "Placement Cell Administration"
admin.site.site_title = "UPC JMI Admin Portal"
admin.site.index_title = "University Placement Cell, Jamia Millia Islamia"
