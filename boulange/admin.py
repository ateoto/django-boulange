from django.contrib import admin

from . import models

admin.site.register(models.InventoryItem)
admin.site.register(models.OnHandInventoryItem)