from django.db import models
from djmoney.models.fields import MoneyField
import uuid


class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('user.CustomUser', on_delete=models.SET_NULL,
                             null=True)
    amount = MoneyField(max_digits=8, decimal_places=2, default_currency='EUR')
    refunded = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
