from django.core.management.base import BaseCommand

from django.contrib.auth.models import User

from transactions.models import Transaction
from core.utils import print_green

class Command(BaseCommand):
    params_user = {
        'username':'celero',
        'email':'admin@celero.com.br',
        'is_superuser':True, 
    }
    password = 'celero2018'

    def create_user(self):
        user, created  = User.objects.get_or_create(**self.params_user)
        if not created:
            Transaction.objects.filter(wallet__user=user).delete()
            return user 
        user.set_password(self.password)
        user.save()
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
        print('populating db...')
        print_green('Ok')
        
    def handle(self, **options):
        self._initial_handle()
        