from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Item, Purchase

# Register your models here
admin.site.register(Item)
admin.site.register(Purchase)
