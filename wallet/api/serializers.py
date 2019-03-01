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
        # write some logic that don't be inside model object validation rules 
        return data

    def create(self, validated_data):
        try:
            request = self.context.get('request')
            wallet = request.user.wallet
            transaction = self.Meta.model.objects.create(**validated_data, wallet=wallet)   
        except Exception as e:
            raise serializers.ValidationError(e)
        return transaction