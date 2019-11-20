from rest_framework.generics import ListAPIView
from .models import JobTitle
from .serializers import JobTitleSerializer


class JobListViews(ListAPIView):
    queryset = JobTitle.objects.all()
    serializer_class = JobTitleSerializer

    permission_classes = ()
    authentication_classes = ()
