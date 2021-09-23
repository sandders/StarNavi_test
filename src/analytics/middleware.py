from django.utils.timezone import now
from rest_framework_simplejwt.authentication import JWTAuthentication


class LastRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = JWTAuthentication().authenticate(request)
        if user:
            user = user[0]
            if user.is_authenticated:
                user.last_request = now()
                user.save(update_fields=['last_request'])
        response = self.get_response(request)
        return response
