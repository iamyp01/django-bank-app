from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null=False, default='')
    last_name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=30, default='')
    current_balance = models.IntegerField(default=0)
    total_tranfers = models.IntegerField(default=0)

class Transfer(models.Model):
    send_by = models.ForeignKey(Customer, related_name='sender', on_delete=models.CASCADE)
    send_to = models.ForeignKey(Customer, related_name='receiver', on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

