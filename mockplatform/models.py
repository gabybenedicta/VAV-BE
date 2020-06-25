from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class CardHolderDetails(models.Model):
    uid = models.CharField(max_length=100, unique=True)
    public_key= models.CharField(max_length=100)

class Invoice(models.Model):
    STATUS_CHOICES =( 
    ("C", "CREATED"), 
    ("I", "IN PROCESS"), 
    ("S", "SUCCESS"), 
    ("F", "FAILED"),
    ) 
  
    seller_id = models.CharField(max_length=100)
    buyer_id = models.CharField(max_length=100)
    amount = models.FloatField()
    description = models.CharField(max_length=150, default=None)
    transaction_status = models.CharField(
        choices= STATUS_CHOICES,
        default= "C",
        max_length = 1
    )
    currency= models.CharField(max_length=3, default= "SGD")
    transaction_id = models.CharField(max_length=150, default="")
   
