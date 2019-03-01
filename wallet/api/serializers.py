from rest_framework import serializers

from ..models import Transaction, Wallet 


class ListTransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('name', 'value', 'type_transaction')
        read_only_fields = ("wallet", )

    def validate(self, data):
        from constants import OUT, IN  
        type_transaction = data.get('type_transaction', None)
        if type_transaction not in [OUT, IN]:
            raise serializers.ValidationError("Invalid type transaction !")

    def create(self, validated_data):
        request = self.context.get('request')
        wallet = request.user.wallet
        transaction = self.Meta.model.objects.create(**validated_data, wallet=wallet)   
        return transaction


# class CreateTransactionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Transaction
#         fields = ('name', 'type_transaction', 'value')

#     def validate(self, data):
#         from constants import OUT, IN  
#         type_transaction = data.get('type_transaction', None)
#         if type_transaction not in [OUT, IN]:
#             raise serializers.ValidationError("Invalid type transaction !")
            

#     def create(self, validated_data):
#         request = self.context.get('request')
#         wallet = request.user.wallet
#         transaction = self.Meta.model.objects.create(**validated_data, wallet=wallet)   
#         return transaction