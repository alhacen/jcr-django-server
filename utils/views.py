__all__ = ['SignUpViewBase']
from django.contrib.auth.models import User
from django.utils.timezone import datetime
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.conf.global_settings import DEBUG
from rest_framework.response import Response

from core.auth.models import Account
from utils.api import OpenAPI, bad_request, response
from utils.classes import FakeModel
from utils.crypto import generate_hash


class SignUpViewBase(OpenAPI):
    user = FakeModel()
    account = FakeModel()

    def create_user(self, request):
        account_data = dict(request.data['account'])

        self.user = User.objects.create_user(
            username=generate_hash('sha256', str(account_data['phone']))[:8],
            password=account_data.get('password',
                                      generate_hash('sha256', f"{account_data['phone']} {datetime.now().__str__()}")
                                      ),
            email=account_data.get('email', None)
        )
        account_data.pop('password', None)

        self.account = Account.objects.create(
            **account_data,
            user=self.user,
            type=self.account_type,
        )

    def create_extra(self, request):
        raise NotImplementedError

    def post(self, request):
        """
        {
            account: {
                phone: str(10),
                alternate_number?: str(10),
                email?: email,
                password?: str(),
            }
        }
        :param request:
        :return:
        """
        to_delete = True

        try:
            self.create_user(request)
            self.create_extra(request)

            to_delete = False
            return response('User Created')

        except ValidationError as error:
            return Response(error, status=404)

        except KeyError as err:
            print(err)
            return bad_request('Some details are missing')

        except IntegrityError as err:
            print(err)
            return bad_request('The user with phone/email exist')

        except Exception as err:
            if DEBUG:
                raise
            else:
                print(err)

            return response('Unknown error occured', 500)

        finally:
            if to_delete:
                self.user.delete()
                print('Deleted wrong data')
