from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

from .constants import IN, OUT


# Create your models here.
class Wallet(models.Model):
    user = models.OneToOneField(User, related_name='wallet', on_delete=models.CASCADE, null=True)


class Transaction(models.Model):
    TYPES_TRANSACTION = (   
        (OUT, 'OUT'),  
        (IN, 'IN'),
    )
    name = models.CharField(max_length=100)
    value = models.FloatField()
    type_transaction = models.SmallIntegerField(choices=TYPES_TRANSACTION)
    wallet = models.ForeignKey(Wallet, related_name='transactions', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def _set_value_by_type_transaction(self):
        if self.value > 0:
            if self.type_transaction == IN:
                pass
            elif self.type_transaction == OUT:
                self.value = -self.value
            return float(self.value)
        else:
            raise Exception('input value field must be positive !')
        
    def _check_type_transaction(self):
        if self.type_transaction not in [OUT, IN]:
            raise Exception('invalid value to type_transaction, must be 0 or 1 !')
    
    def _check_wallet(self):
        if not self.wallet:
            raise Exception('wallet field cannot be null')

    @property
    def presentation_value(self):
        value = ' R${:.2f}'
        if self.type_transaction == IN:
            value = '+' + value.format(abs(self.value))
        elif self.type_transaction == OUT:
            value = '-' + value.format(abs(self.value))
        return value 

    def save(self, *args, **kwargs):
        if not self.pk:
            self._check_wallet()
            self._check_type_transaction()
            self._set_value_by_type_transaction()
        super().save(*args, **kwargs)
    
    def __str__(self):
        value_to_presentation = 'R${:2f}'.format(abs(self.value))
        return '{0} - {1}'.format(self.name, value_to_presentation)




    
    