from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class CardHolderDetails(models.Model):
    uid = models.CharField(max_length=100, unique=True)
    public_key= models.CharField(max_length=100)

class Invoice(models.Model):
    seller_id = models.IntegerField()
    buyer_id = models.IntegerField()
    amount = models.FloatField()
    description = models.CharField(max_length=150, default=None)
