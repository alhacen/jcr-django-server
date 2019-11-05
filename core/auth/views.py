__all__ = [
    'SignInWithOTPView', 'SignInWithPasswordView',
    'send_otp_view', 'user_meta_api_view', 'ForgotPasswordView'
]
from datetime import timedelta
from random import randint

from django.core.signing import TimestampSigner, SignatureExpired
from django.contrib.auth import authenticate
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from utils.api import *
from .models import Account
from .helpers import send_otp

signer = TimestampSigner()


class SignInView(OpenAPI):
    """Base class for getting JWT tokens of 'authenticated' user"""
    user = None

    def post(self, request):
        raise NotImplementedError

    def get_user(self, request):
        """Gets user from given email/phone"""
        username = request.data['username']

        self.user = Account.objects.select_related('user') \
            .get(Q(email=username) | Q(phone=username)).user

    def get_token(self):
        # TODO: Check is instance of
        if not self.user:
            return not_found('User not found')

        refresh = RefreshToken.for_user(self.user)
        access_token = refresh.access_token

        return Response({
            'refresh': str(refresh),
            'access': str(access_token)
        })


@api_view(['GET'])
def user_meta_api_view(request):
    name = request.user.get_full_name()
    if request.user.account.company:
        name += f' ({request.user.account.company})'

    return Response({
        'name': name,
        'email': request.user.account.email,
        'phone': request.user.account.phone,
        'type': request.user.account.type
    })


class SignInWithPasswordView(SignInView):
    """SignIn user using email/phone and password"""

    def post(self, request):
        """

        :param request:
            username: str -> Email or phone number of user
            password: str -> Password for the user
        :return: JWT Tokens and user meta
        """
        try:
            password = request.data['password']
            self.get_user(request)

            if authenticate(username=self.user.username, password=password) is not None:
                return self.get_token()

            return bad_request('Incorrect credentials')

        except Account.DoesNotExist:
            return bad_request('User does not exist')

        except KeyError:
            return bad_request('Either of email/phone or password not provided')


class SignInWithOTPView(SignInView):
    """SignIn user using email/phone and OTP"""

    def post(self, request):
        """
        :param request:
            username: str -> Email or phone number of user
            otp: str -> OTP
        :return: JWT Tokens and user meta
        """
        try:
            otp_given = request.data['otp']
            self.get_user(request)

            otp_generated = self.user.account.otp
            print(otp_generated)
            if str(otp_given) == str(signer.unsign(otp_generated, max_age=timedelta(minutes=15))):
                return self.get_token()

            return bad_request('Invalid credentials')

        except SignatureExpired:
            return bad_request('OTP expired')

        except KeyError as err:
            print(err)
            return bad_request('Either of email/phone or otp not provided')


@api_view(['POST'])
@open_api
def send_otp_view(request):
    """View which handel sending otp to Users"""
    phone = None

    try:
        username = request.data['username']
        account = Account.objects.select_related('user') \
            .get(Q(email=username) | Q(phone=username))
        otp = None

        if account.otp:
            try:
                signer.unsign(account.otp, max_age=timedelta(minutes=15))
                otp = account.otp
            except SignatureExpired:
                pass

        if not otp:
            otp = signer.sign(randint(1111, 9999))

        account.otp = otp
        account.save()

        # Actual otp sending
        status, mess = send_otp(account)

        if status:
            return response(mess)
        else:
            return bad_request(mess)

    except KeyError:
        return bad_request('username should be provided')
    except Account.DoesNotExist:
        return bad_request(f'No account exist with phone/email {phone}')


class ForgotPasswordView(OpenAPI):

    def __init__(self, *args, **kwargs):
        super(ForgotPasswordView, self).__init__(*args, **kwargs)
        self.user = None

    def get_user(self, request):
        """Gets user from given email/phone"""
        username = request.data['username']

        self.user = Account.objects.select_related('user') \
            .get(Q(email=username) | Q(phone=username)).user

    def post(self, request):
        """
        :param request:
            username: str -> Email or phone number of user
            otp: str -> OTP
        :return: JWT Tokens and user meta
        """
        try:
            otp_given = request.data['otp']
            new_password = request.data['password']
            self.get_user(request)

            otp_generated = self.user.account.otp
            if str(otp_given) == str(signer.unsign(otp_generated, max_age=timedelta(minutes=15))):
                self.user.set_password(new_password)
                self.user.save()
                return response('Password change successful')

            return bad_request('Invalid credentials')

        except SignatureExpired:
            return bad_request('OTP expired')

        except KeyError as err:
            return bad_request('Either of email/phone or otp not provided')
