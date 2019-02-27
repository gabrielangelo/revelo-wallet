from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import EmailAuthenticateSerializer


class EmailObtainAuthTokenView(ObtainAuthToken):
    serializer_class = EmailAuthenticateSerializer

