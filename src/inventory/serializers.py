from rest_framework import serializers
from .models import Contact, Item, Supplier

class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ['id', 'address', 'phone', 'email']

class SupplierSerializer(serializers.ModelSerializer):
    contact_info = ContactSerializer()

    class Meta:
        model = Supplier
        fields = ['id', 'name', 'contact_info', 'items']
        
    def create(self, validated_data):
        contact_data = validated_data.pop('contact_info')
        items_data = validated_data.pop('items')
        contact = Contact.objects.create(**contact_data)
        supplier = Supplier.objects.create(contact_info=contact, **validated_data)
        supplier.items.set(items_data)
        return supplier

    
    def update(self, instance, validated_data):
        contact_data = validated_data.pop('contact_info')
        items_data = validated_data.pop('items')
        contact = instance.contact_info

        instance.name = validated_data.get('name', instance.name)
        instance.save()

        contact.address = contact_data.get('address', contact.address)
        contact.phone = contact_data.get('phone', contact.phone)
        contact.email = contact_data.get('email', contact.email)
        contact.save()

        instance.items.set(items_data)

        return instance

class ItemSerializer(serializers.ModelSerializer):
    suppliers = SupplierSerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'price', 'date_added', 'suppliers']

