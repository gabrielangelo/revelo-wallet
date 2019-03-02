from django.contrib.auth.models import User
from django.test import TestCase
from django.db.models.fields.related_descriptors import ForwardManyToOneDescriptor
from django.core.exceptions import ValidationError
from model_mommy import mommy

from ..models import Transaction, Wallet
from ..constants import IN_TRANSACTION, OUT_TRANSACTION


class TransactionTest(TestCase):

        def test_signal_by_type_transaction(self):
            wallet = mommy.make(Wallet)
            transaction1 = mommy.make(
                Transaction, 
                type_transaction=IN_TRANSACTION, 
                wallet=wallet, 
                value=10.00
            )
            transaction2 = mommy.make(
                Transaction, 
                type_transaction=OUT_TRANSACTION,
                wallet=wallet, 
                value=5.00
            )
            self.assertTrue(transaction1.value > 0)
            self.assertTrue(transaction2.value < 0)

        def test_wallet_constraint_not_null(self):
            from django.db import IntegrityError
            with self.assertRaises(IntegrityError):
                mommy.make(
                    Transaction, 
                    wallet=None
                )
        
        def test_transaction_presentation_value(self):
            transaction_positive = mommy.make(
                Transaction, 
                value=10.00, 
                type_transaction=IN_TRANSACTION
            )

            transaction_negative = mommy.make(
                Transaction, 
                value=15.00, 
                type_transaction=OUT_TRANSACTION
            )
            self.assertEqual(
                transaction_positive.presentation_value, 
                '+ R${:.2f}'.format(transaction_positive.value))
            
            self.assertEqual(transaction_negative.presentation_value, 
                '- R${:.2f}'.format(abs(transaction_negative.value)))

        def test_transaction_check_type_transaction(self):
            with self.assertRaises(ValidationError):
                mommy.make(
                    Transaction, 
                    type_transaction=5
                )

        def test_transaction_negative_value_input(self):
            with self.assertRaises(ValidationError):
                mommy.make(
                    Transaction,
                    value=-10.00
                )

        def test_transaction_many_to_one_relationship(self):
            wallet = mommy.make(Wallet)
            transactions = [
                mommy.make(
                    Transaction,
                    wallet=wallet
                ) for i in range(0, 10)
            ]
            self.assertTrue(list(wallet.transactions.all()) == transactions)


class WalletTest(TestCase):
    def test_wallet_creation_during_user_creation_signal(self):
        user = mommy.make(User)
        self.assertTrue(user.wallet is not None)

        
    
        
        