from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from account.views import registration_view, LoginTokenObtainView

app_name = 'account'

urlpatterns = [
    path('register', registration_view, name='api-register'),
    path('token/login', LoginTokenObtainView.as_view(), name='api-token-login'),
    path('token/refresh', TokenRefreshView.as_view(), name='api-token-refresh'),
]
