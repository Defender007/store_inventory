from django.test import TestCase
from rest_framework.test import APIClient
from .models import Supplier, Item

class InventoryTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.supplier = Supplier.objects.create(name="Big Supplier", contact_info="USA-009-123")
        self.item = Item.objects.create(name="First Item", description="A sample item", price=24.99)
        self.item.suppliers.add(self.supplier)

    def test_create_item(self):
        response = self.client.post('/api/items/', {'name': 'New Item', 'description': 'A brand new item', 'price': 40.00})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['price'], "40.00")
        
    def test_get_items(self):
        response = self.client.get('/api/items/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(float(response.data[0]['price']), 24.99)
    
    def test_get_item_by_id(self):
        response = self.client.get('/api/items/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'First Item')
        self.assertEqual(response.data['suppliers'][0], {'id': 1, 'name': 'Big Supplier', 'contact_info': 'USA-009-123', 'items': [1]})

    def test_get_suppliers(self):
        response = self.client.get('/api/suppliers/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
    
    def test_get_supplier_id(self):
        response = self.client.get('/api/suppliers/1/', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'id': 1, 'name': 'Big Supplier', 'contact_info': 'USA-009-123', 'items': [1]})
