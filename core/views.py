from admin_auto_filters.views import AutocompleteJsonView
from rest_framework.generics import ListAPIView

from .models import JobTitle
from .serializers import JobTitleSerializer


class JobListViews(ListAPIView):
    queryset = JobTitle.objects.all()
    serializer_class = JobTitleSerializer

    permission_classes = ()
    authentication_classes = ()


class JobTitleSearchView(AutocompleteJsonView):
    def get_queryset(self):
        queryset = JobTitle.objects.all().order_by('title')
        return queryset
