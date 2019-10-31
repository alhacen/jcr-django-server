from django.core.management.base import BaseCommand
from core.models import JobTitle
from utils.choices import JobProfilesChoices


class Command(BaseCommand):
    def handle(self, *args, **options):
        for x in JobProfilesChoices.choices:
            try:
                JobTitle.objects.create(title=x[1])
                print(x[1])
            except Exception as err:
                print(err)
