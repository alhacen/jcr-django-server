import os
import pyexcel as pe

from django.conf import settings
from django.core.management.base import BaseCommand

from core.models import JobTitle
from seeker.models import Seeker
from django.contrib.auth.models import User
from django.utils.timezone import datetime

from core.auth.models import Account
from utils.choices import EDUCATIONAL_QUALIFICATION_CHOICES
from utils.crypto import generate_hash

col = {
    'mobile': 1,
    'name': 2,
    'experience': 3,
    'dob': 4,
    'address': 5,
    'father': 6,
    'aadhar': 8,
    'job': 9,
    'education': 10,
}

extra_job_qualification = {
    'Graduate (B.A.,B.Com., B.Sc.)': 'Graduate (B.Sc., B.A., B.Com.)',
    '10th Pass': '10th pass',
    '12th Pass': '12th pass',
    'Post Graduate (Any Stream)': 'Post graduate (Any stream)',
    'Below Class 5th': 'BELOW 5th Class',
    'MBA / PGDM (Any Stream)': 'MBA/PGDM (Any Stream)',
    '8th - 10th Class': 'Class 5th to 9th'
}

extra_experience = {
    'Fresher': 0,
    'Experience (Above 5 yrs)': 6,
    'Experience (0 to 1 yr)': 1,
    'Experience (2 to 5 yrs)': 4,
    'Experience (1 to 2 yrs)': 2
}

OTHER_JOB = JobTitle.objects.get(title='Other')

extra_job_title = {
    'Security Guard': JobTitle.objects.get(title='Security Staff'),
    'Others': OTHER_JOB,
    'Driver (Heavy Vehicles - Bus, Truck, etc.)': JobTitle.objects.get(title='Driver (Heavy Vehicles - Bus, Truck, Trailer, etc.)')
}


class TestRow(object):
    def __init__(self, sheet, i):
        for _col in col:
            setattr(
                self,
                _col,
                getattr(self, 'test_' + _col)(sheet[i, col[_col]])
            )

    def test_name(self, name):
        return name

    def test_mobile(self, mobile):
        mobile = str(mobile).replace(' ', '')

        if len(mobile) != 10:
            if len(mobile) == 12 and mobile[:2] == '91':
                mobile = mobile[2:]
            elif len(mobile) == 13 and mobile[:3] == '+91':
                mobile = mobile[3:]
            elif len(mobile) == 11 and mobile[0] == '0':
                mobile = mobile[1:]
            elif '*' in mobile:
                mobile = self.test_mobile(mobile.split('*')[0])
            else:
                raise ValueError(f'Mobile number {mobile} is not correct')

        return mobile

    def test_experience(self, experience):
        if experience == '':
            return None

        if experience not in extra_experience:
            raise ValueError(f'{experience} is not in experience')

        return extra_experience[experience]

    def test_dob(self, dob):

        if type(dob) == str:
            if len(dob) == 0:
                return None

            dob = datetime.strptime(dob, '%Y-%m-%dT00:00:00Z')

        try:
            return dob.strftime("%Y-%m-%d")
        except AttributeError:
            return None

    def test_address(self, address):
        return address

    def test_father(self, father):
        return father.title()

    def test_aadhar(self, aadhar):
        aadhar = str(aadhar)
        if len(aadhar) != 12:
            return None

        return aadhar

    def test_job(self, job):
        try:
            return JobTitle.objects.get(title=job)
        except JobTitle.DoesNotExist:
            if job == '':
                return OTHER_JOB
            elif job in extra_job_title:
                return extra_job_title[job]

            raise ValueError(f'{job} does not exist')

    def test_education(self, education):
        for x in EDUCATIONAL_QUALIFICATION_CHOICES:
            if education == '':
                return None

            if x[0] == education:
                return education
            elif education in extra_job_qualification:
                return extra_job_qualification[education]

        raise ValueError(f'{education} is not in education')

    def show(self):
        data = ''
        for _col in col:
            data += ' | ' + _col + ': ' + str(getattr(self, _col))

        return data[2:]


def create(row):
    user = User.objects.create_user(
        username=row.mobile,
        password=generate_hash('sha256', f"{row.mobile} {datetime.now().__str__()}"),
        email=None
    )
    user.first_name = row.name.title()
    user.save()

    account = Account.objects.create(
        user=user,
        type=Account.SEEKER,
        phone=row.mobile
    )

    Seeker.objects.create(
        account=account,
        fathers_name=row.father,
        dob=row.dob,
        address=row.address,
        job_title=row.job,
        aadhar=row.aadhar,
        educational_qualification=row.education,
    )


class Command(BaseCommand):
    def handle(self, *args, **options):
        sheet = pe.get_sheet(file_name=os.path.join(
            settings.BASE_DIR,
            'data.xlsx'
        ), name_columns_by_row=0)

        err_count = 0
        for i in range(len(sheet)):
            try:
                x = TestRow(sheet, i)
                create(x)
            except Exception as err:
                print(err)
                print(sheet[i])
                print('-' * 50)
                err_count += 1

        print('err_count', err_count)
