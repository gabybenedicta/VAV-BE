from django.contrib import admin
from .models import CardHolderDetails, Invoice

# Register your models here.

admin.site.register(CardHolderDetails)
admin.site.register(Invoice)
