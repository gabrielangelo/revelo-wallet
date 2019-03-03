from django.urls import reverse, resolve
from django.contrib.auth.models import User

from model_mommy import mommy
from rest_framework.test import APIClient, APITestCase
from rest_framework.authtoken.models import Token


class ClientNativeTokenAuthorizationMixin(object):
    """s
    Adds helpful methods to create users and
    logged users
    """
    def make_authorized_client(self, user):
        client = APIClient()
        token = Token.objects.create(user=user)
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        return client

    def make_anonymous_client(self):
        return APIClient()

    def make_unauthorized_client(self):
        return APIClient()
        
    def make_user(self):
        return User.objects.create(
            email='whatever@xxx.com', 
            password='123'
        )
        

def resolve_by_name(name, **kwargs): 
    url = reverse(name, kwargs=kwargs) 
    return resolve(url)