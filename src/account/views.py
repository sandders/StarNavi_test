from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.views import TokenViewBase

from account.serializers import RegistrationSerializer, LoginTokenObtainSerializer


class AccountCreateAPIView(CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = []


class LoginTokenObtainView(TokenViewBase):
    serializer_class = LoginTokenObtainSerializer
    permission_classes = []
