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


class Products(models.Model):
    user = models.ForeignKey(PlatformUser, related_name='products', on_delete=models.CASCADE)
    date = models.DateField()
    name = models.CharField(max_length=100)
    description = models.TextField()
