from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from decimal import Decimal

from .constants import IN_TRANSACTION, OUT_TRANSACTION


# Create your models here.
class Wallet(models.Model):
    user = models.OneToOneField(User, related_name='wallet', on_delete=models.CASCADE, null=True)


class Transaction(models.Model):
    TYPES_TRANSACTION = (   
        (OUT_TRANSACTION, 'OUT'),  
        (IN_TRANSACTION, 'IN'),
    )
    name = models.CharField(max_length=100)
    value = models.DecimalField(decimal_places=2, max_digits=12)
    type_transaction = models.SmallIntegerField(choices=TYPES_TRANSACTION)
    wallet = models.ForeignKey(Wallet, related_name='transactions', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    @property
    def presentation_value(self):
        value = ' R${:.2f}'
        if self.type_transaction == IN_TRANSACTION:
            value = '+' + value.format(abs(self.value))
        elif self.type_transaction == OUT_TRANSACTION:
            value = '-' + value.format(abs(self.value))
        return value 

    def _set_value_by_type_transaction(self):
        if self.type_transaction == IN_TRANSACTION:
            pass
        elif self.type_transaction == OUT_TRANSACTION:
            self.value = -self.value
        return Decimal(self.value)  
        
    def _check_type_transaction(self):
        if self.type_transaction not in [OUT_TRANSACTION, IN_TRANSACTION]:
            raise ValidationError('invalid value to type_transaction, must be 0 or 1 !')
    
    def _check_signal_value(self):
        if self.value < 0:
            raise ValidationError('set value must be positive')

    def save(self, *args, **kwargs):
        if not self.pk:
            self._check_signal_value()
            self._check_type_transaction()
            self._set_value_by_type_transaction()
        super().save(*args, **kwargs)
    
    def __str__(self):
        value_to_presentation = 'R${:.2f}'.format(abs(self.value))
        return '{0} - {1}'.format(self.name, value_to_presentation)




    
    