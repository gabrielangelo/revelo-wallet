from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from ..models import Transaction
from .serializers import ListTransactionsSerializer, CreateTransactionSerializer


class TransactionsViewSet(
    GenericViewSet,
    mixins.CreateModelMixin, 
    mixins.ListModelMixin,  
    mixins.RetrieveModelMixin):
    
    permission_classes = (IsAuthenticated, )
    serializer_class = CreateTransactionSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_fields = ('name', 'type_transaction')
    ordering_fields = ('name', 'value') 
    
    def get_serializer_class(self):
        request = self.request
        return ListTransactionsSerializer
    
    # def get_serializer(self):
    #     return CreateTransactionSerializer

    def get_queryset(self):
        user = self.request.user
        return Transaction.objects.filter(wallet__user=user)
