from django.core.management.base import BaseCommand

from django.contrib.auth.models import User

from wallet.models import Transaction


class Command(BaseCommand):
    params_user = {
        'username':'celero',
        'email':'admin@celero.com.br', 
        'password':'celero2018', 
        'is_superuser':True
    }
    
    def create_user(self):
        user, created  = User.objects.get_or_create(**self.params_user)
        if created:
            Transaction.objects.filter(wallet__user=user).delete()
            return user 
        return user 
    
    def create_transactions(self, user):
        from decimal import Decimal
        from os import urandom
        import binascii
        from random import randrange
        user_transactions = [
            Transaction(
                value=Decimal(randrange(10, 100000))/100, 
                type_transaction=int(randrange(0,2)), 
                name=binascii.hexlify(urandom(16)), 
                wallet=user.wallet
            ) for i in range(30)
        ]
        Transaction.objects.bulk_create(user_transactions)
    

    def _initial_handle(self): 
        self.create_transactions(self.create_user())

    def handle(self, **options):
        self._initial_handle()