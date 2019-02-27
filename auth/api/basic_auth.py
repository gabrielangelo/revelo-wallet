from django.contrib.auth.models import User
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions


class EmailAuthentication(BaseAuthentication):
    def authenticate(self, request, **kwargs):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        if not email and not password:
            if 'email' in kwargs.keys() and 'password' in kwargs.keys():
                email = kwargs['email']
                password = kwargs['password']
            else:
                return None

        try:
            user = User.objects.get(email=email, is_active=True)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')
        request_url = request.META.get('PATH_INFO', None)

        if ('admin' in request_url) and (not user.is_staff):
            return None

        if user.check_password(password):
            return user
        return None
