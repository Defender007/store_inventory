from rest_framework import serializers
from .models import Supplier, Item

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id', 'name', 'contact_info', 'items']

class ItemSerializer(serializers.ModelSerializer):
    suppliers = SupplierSerializer(many=True, read_only=True)
    
    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'price', 'date_added', 'suppliers']
