__all__ = [
    'response', 'bad_request', 'not_found',
    'open_api', 'OpenAPI'
]
from rest_framework.response import Response
from rest_framework import status as drf_status
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes


def response(detail, status=drf_status.HTTP_200_OK):
    """
    :param detail: str -> message to send
    :param status: int -> HTTP response code
    :return: Response with details
    """
    return Response({
        'detail': detail
    }, status=status)


def bad_request(detail):
    """
    Bad response helper

    :param detail: str -> details
    :return: Response with details and HTTP_400_BAD_REQUEST
    """
    return response(detail, status=drf_status.HTTP_400_BAD_REQUEST)


def not_found(detail):
    """
    Bad response helper

    :param detail: str -> details
    :return: Response with details and HTTP_400_BAD_REQUEST
    """
    return response(detail, status=drf_status.HTTP_404_NOT_FOUND)


def open_api(func):
    """Remove default permissions"""

    return permission_classes(())(func)


class OpenAPI(APIView):
    permission_classes = []
    authentication_classes = []
