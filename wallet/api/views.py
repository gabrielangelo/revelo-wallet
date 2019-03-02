from django.core.exceptions import SuspiciousOperation

from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.filters import OrderingFilter
from rest_framework import status
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from ..models import Transaction
from .serializers import ListTransactionsSerializer, CreateTransactionSerializer
from ..utils import format_error_payload, format_success_payload


class ListCreateViewset(GenericViewSet,
    mixins.CreateModelMixin, 
    mixins.ListModelMixin):
    list_serializer = None
    create_serializer = None
    
    def make_serializers_list_by_http_verbs(self):
        list_serializers = {
                'get':self.list_serializer, 
                'post':self.create_serializer
            }
        return list_serializers

    def get_serializer_by_http_verb(self, http_verb):
        try:
            list_serializers = self.make_serializers_list_by_http_verbs()
            serializer = list_serializers[http_verb.lower()]
        except KeyError:
            raise SuspiciousOperation('attemt http verb denied !')
        return serializer


class TransactionsViewSet(ListCreateViewset):
    permission_classes = (IsAuthenticated, )
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_fields = ('name', 'type_transaction')
    ordering_fields = ('name', 'value') 
    list_serializer = ListTransactionsSerializer
    create_serializer = CreateTransactionSerializer
    ordering = ('created_at', )
     
    def get_serializer_class(self):
       serializer = self.get_serializer_by_http_verb(self.request.method)
       return serializer

    def get_queryset(self):
        user = self.request.user
        return Transaction.objects.filter(wallet__user=user)
