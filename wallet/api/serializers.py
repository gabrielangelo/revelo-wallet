from rest_framework import serializers

from ..models import Transaction, Wallet 


class ListTransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('name', 'value')

    def to_representation(self, obj):
        return {
            "name": obj.name, 
            "value": obj.presentation_value, 
        }


class CreateTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('name', 'type_transaction', 'value')

    def validate(self, data):
        value = data.get('value', None)
        if value < 0:
            raise serializers.ValidationError('value must be positive !')
        return data

    def create(self, validated_data):
        request = self.context.get('request')
        wallet = request.user.wallet
        transaction = self.Meta.model.objects.create(**validated_data, wallet=wallet)
        return transaction