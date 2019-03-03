from django.core.exceptions import SuspiciousOperation
from django.utils.translation import gettext as _

from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.filters import OrderingFilter
from rest_framework import status
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from ..models import Transaction
from .serializers import ListTransactionsSerializer, CreateTransactionSerializer


class ListCreateViewset(GenericViewSet,
    mixins.CreateModelMixin, 
    mixins.ListModelMixin):
    list_serializer = None
    create_serializer = None
    
    def make_serializers_list_by_http_verbs(self):
        list_serializers = {
                u'get':self.list_serializer, 
                u'post':self.create_serializer
            }
        return list_serializers

    def get_serializer_by_http_verb(self, http_verb):
        try:
            list_serializers = self.make_serializers_list_by_http_verbs()
            serializer = list_serializers[http_verb.lower()]
        except KeyError:
            raise SuspiciousOperation(_(u'attemt http verb denied !'))
        return serializer


class TransactionsViewSet(ListCreateViewset):
    """This endpoint list and create user transactions, below the list params endpoins:\n
            name (string) : filter transaction by name
            type_transaction (integer): filter by type_transaction (can be 0 to spent transactions or 1 to earnings transactions)\n
            ordering: sort the list transaction by some field, the accepeted fields are list below:
                value
                name
                created_at


        List below the fields to create transactions:\n
            value (integer) -> only accpets positive decimal values with 2 places
            name (string)
            type_transaction -> 0 to spent or 1 to eranings
    """ 
    permission_classes = (IsAuthenticated, )
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_fields = (u'name', u'type_transaction')
    ordering_fields = (u'name', u'value') 
    list_serializer = ListTransactionsSerializer
    create_serializer = CreateTransactionSerializer
    ordering = (u'created_at', )
     
    def get_serializer_class(self):
       serializer = self.get_serializer_by_http_verb(self.request.method)
       return serializer

    def get_queryset(self):
        user = self.request.user
        return Transaction.objects.filter(wallet__user=user)
