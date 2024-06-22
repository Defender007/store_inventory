from django.contrib import admin
from .models import Contact, Supplier, Item

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    pass

admin.site.register(Contact, ContactAdmin)

class SupplierAdmin(admin.ModelAdmin):
    pass

admin.site.register(Supplier, SupplierAdmin)

class ItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(Item, ItemAdmin)