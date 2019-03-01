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
    ZERO = '0.00'
    name = models.CharField(max_length=100)
    value = models.FloatField()
    type_transaction = models.SmallIntegerField(choices=TYPES_TRANSACTION)
    wallet = models.ForeignKey(Wallet, related_name='transactions', on_delete=models.CASCADE, null=True)

    @property
    def value_with_signal(self):
        signal = '+ ' if self.type_transaction == self.IN else '- '
        format_value = '{:.2f}'.format(self.value) if self.value > 0 else self.ZERO
        return signal + format_value
    
    # def check_type_transaction(self):
        
    def __str__(self):
        return '{0} - {1}'.format(self.name, self.value_with_signal)




    
    