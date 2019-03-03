from rest_framework import serializers

from ..models import Transaction, Wallet 


class ListTransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = (u'name', u'value')

    def to_representation(self, obj):
        return {
            u'name': obj.name, 
            u'value': obj.presentation_value, 
        }


class CreateTransactionSerializer(serializers.ModelSerializer):
    currency = serializers.CharField(required=False)
    
    class Meta:
        model = Transaction
        fields = (u'name', u'type_transaction', u'value', u'currency')

    def create(self, validated_data):
        request = self.context.get('request')
        wallet = request.user.wallet
        try:
            transaction = self.Meta.model.objects.create(**validated_data, wallet=wallet)
        except Exception as exc:
            raise serializers.ValidationError(dict(exc))
        return transaction