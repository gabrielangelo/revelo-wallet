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
        self.assertGreater(transaction1.value, 0)
        self.assertLess(transaction2.value, 0)

    def test_wallet_constraint_not_null(self):
        from django.db import IntegrityError
        with self.assertRaises(IntegrityError):
            mommy.make(
                Transaction, 
                wallet=None
            )
    
    def test_transaction_presentation_value(self):
        transaction_positive_default_curency = mommy.make(
            Transaction, 
            value=10.00, 
            type_transaction=IN_TRANSACTION
        )

        transaction_negative_default_currency = mommy.make(
            Transaction, 
            value=15.00, 
            type_transaction=OUT_TRANSACTION, 
        )
        transaction_positive_dolar_currency = mommy.make(
            Transaction, 
            value=15.00, 
            type_transaction=IN_TRANSACTION, 
            currency='U$'
        )
        transaction_negative_dolar_currency = mommy.make(
            Transaction, 
            value=15.00, 
            type_transaction=OUT_TRANSACTION, 
            currency='U$'
        )
        transaction_positive_euro_currency = mommy.make(
            Transaction, 
            value=15.00, 
            type_transaction=IN_TRANSACTION, 
            currency='€'
        )
        transaction_negative_euro_currency = mommy.make(
            Transaction, 
            value=15.00, 
            type_transaction=OUT_TRANSACTION, 
            currency='€'
        )

        self.assertEqual(
            transaction_positive_default_curency.presentation_value, 
            '+ R${:.2f}'.format(
                abs(transaction_positive_default_curency.value)))
        
        self.assertEqual(
            transaction_negative_default_currency.presentation_value, 
            '- R${:.2f}'.format(
                abs(transaction_negative_default_currency.value))
                )

        self.assertEqual(transaction_positive_dolar_currency.presentation_value, 
            '+ U${:.2f}'.format(
                abs(transaction_positive_dolar_currency.value))
                )

        self.assertEqual(transaction_negative_dolar_currency.presentation_value,
            '- U${:.2f}'.format(
                abs(transaction_negative_dolar_currency.value))
                )
        
        self.assertEqual(transaction_positive_euro_currency.presentation_value, 
            '+ €{:.2f}'.format(
                abs(transaction_positive_euro_currency.value))
                )

        self.assertEqual(transaction_negative_euro_currency.presentation_value,
            '- €{:.2f}'.format(
                abs(transaction_negative_euro_currency.value))
                )

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
        self.assertEqual(set(wallet.transactions.all()), set(transactions))

    def test_upper_currency_insert_cipher(self):
        low_currency_dolar = 'u$'
        low_currency_real = 'r$'

        transaction_real = mommy.make(
            Transaction, 
            value=10.00, 
            type_transaction=IN_TRANSACTION,
            currency=low_currency_real
        )

        transaction__dolar= mommy.make(
            Transaction, 
            value=15.00, 
            type_transaction=OUT_TRANSACTION, 
            currency=low_currency_dolar
        )

        self.assertEqual(transaction__dolar.currency.lower(), low_currency_dolar )
        self.assertEqual(transaction_real.currency.lower(), low_currency_real)

    def test_invalid_current_symbol(self):         
        with self.assertRaises(ValidationError):
            mommy.make(
                Transaction, 
                value=15.00, 
                type_transaction=OUT_TRANSACTION, 
                currency="whatever"
            )   


class WalletTest(TestCase):
    def test_wallet_creation_during_user_creation_signal(self):
        user = mommy.make(User)
        self.assertTrue(user.wallet is not None)

        
    
        
        