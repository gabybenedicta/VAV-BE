from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class PlatformUser(models.Model):
    # A User Profile model for the user to include the public transaction key
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    transaction_key = models.TextField(default=None)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
						#TODO:
						#check if credit card info is provided, if yes pass the credit card info to a
						#function that generates the public key
            transaction_key = "abc"
            PlatformUser.objects.create(
                user=instance, transaction_key=transaction_key)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class Invoice(models.Model):
    STATUS_CHOICES =( 
    ("C", "CREATED"), 
    ("I", "IN PROCESS"), 
    ("S", "SUCCESS"), 
    ("F", "FAILED"),
    ) 
  
    seller_id = models.IntegerField()
    buyer_id = models.IntegerField()
    amount = models.FloatField()
    description = models.CharField(max_length=150, default=None)
    transaction_status = models.CharField(
        choices= STATUS_CHOICES,
        default= "C",
        max_length = 1
    )
   
