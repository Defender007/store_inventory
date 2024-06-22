from django.db import models


class Contact(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=155)

    def __str__(self):
        return self.email

class Supplier(models.Model):
    name = models.CharField(max_length=255, unique=True)
    contact_info = models.OneToOneField(Contact, related_name="contact", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateField(auto_now_add=True)
    suppliers = models.ManyToManyField(Supplier, related_name='items')

    def __str__(self):
        return self.name
