from rest_framework import serializers
from .models import Seeker, SeekerDocuments
from core.models import JobApplication


class SeekerSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='account.user.first_name')
    status = serializers.SerializerMethodField()

    def __init__(self, *args, **kwargs):
        self._job_id = kwargs.pop('job_id', None)

        super(SeekerSerializer, self).__init__(*args, **kwargs)

    def get_status(self, instance):
        try:
            return JobApplication.objects.get(
                seeker=instance,
                job_id=self._job_id
            ).status
        except Exception:
            return 'U'

    class Meta:
        model = Seeker
        exclude = ('account',)


class SeekerDocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('title', 'desc', 'file', 'embed', 'link')
        model = SeekerDocuments
