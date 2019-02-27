from django.contrib.auth.backends import ModelBackend
from django.models.

class EmailBackend(ModelBackend):
    def authenticate(self, username=None, password=None):
        try:
            user = User.objects.get(email=username)
        except (User.DoesNotExist):
            return None
        else:
            if user.check_password(password):
                return user