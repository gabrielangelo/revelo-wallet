from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User


class EmailBackend(ModelBackend):
    def authenticate(self, *args, **kwargs):
        try:
            username = kwargs.get('username', None)
            password = kwargs.get('password', None)
            if (username is None) or (password is None):
                return None 
            user = User.objects.get(email=username)
        except (User.DoesNotExist):
            return None
        else:
            if user.check_password(password):
                return user