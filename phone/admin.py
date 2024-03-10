from django.contrib import admin

from phone.models import ItemDetails, Items

# Register your models here.

admin.site.register(Items)
admin.site.register(ItemDetails)
