from django.conf.urls import url

from rest_framework_jwt.views import obtain_jwt_token
from .serializers import EmailJWTSerializer

urlpatterns = [
    url(r'^obtain-token', obtain_jwt_token),
]

