from django.conf.urls import url

from .views import EmailObtainAuthTokenView

urlpatterns = [
    url(r'auth', EmailObtainAuthTokenView.as_view(), name='auth')
]
