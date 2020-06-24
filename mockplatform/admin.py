from django.contrib import admin
from .models import PlatformUser
from .models import Invoice

# Register your models here.

admin.site.register(PlatformUser)
admin.site.register(Invoice)
