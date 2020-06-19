from django.contrib import admin
from .models import PlatformUser
from .models import Products

# Register your models here.

admin.site.register(PlatformUser)
admin.site.register(Products)
