from rest_framework_simplejwt import views as jwt_views
from django.urls import path

from .views import *


urlpatterns = [
    path('sign-in/password/', SignInWithPasswordView.as_view(), name='sign-in-with-password'),
    path('meta/', user_meta_api_view, name='user-meta'),
    path('sign-in/otp/', SignInWithOTPView.as_view(), name='sign-in-with-otp'),
    path('sign-in/otp/send/', send_otp_view, name='send-otp'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token-refresh'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='token-refresh')

]

app_name = 'core'
