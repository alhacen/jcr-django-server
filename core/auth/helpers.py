__all__ = ['send_otp']
from django.conf import settings
from django.core.signing import TimestampSigner

signer = TimestampSigner()


def send_otp(account):
    """
    Sends OTP to Email and Phone

    :param account: core.auth.Account
    :return: bool, str -> (Status of sending; Message)
    """
    mess = 'Sent otp '
    if settings.DEBUG:
        mess += f'{signer.unsign(account.otp)} '

    mess += f'to {account.user.get_full_name()} on {account.phone} '

    if account.email:
        mess += f'to {account.email}'

    return True, mess
