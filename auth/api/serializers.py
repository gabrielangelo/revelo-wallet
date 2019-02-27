from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied

from basic_auth import EmailAuthentication as auth_module


class EmailAuthenticateSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(trim_whitespace=False)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = auth_module.authenticate(
                request=self.context.get('request'),
                email=email, 
                password=password
            )

            if not user:
                msg = 'Unable to log in with provided credentials.'
                raise PermissionDenied(detail=msg)
        else:
            msg = 'Must include "username" and "password".'
            raise PermissionDenied(detail=msg)
        attrs['user'] = user
        return attrs