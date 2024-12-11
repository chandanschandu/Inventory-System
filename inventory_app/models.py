from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Purchase {self.id} by {self.user.username}"

class Item(models.Model):
    ITEM_TYPES = [
        ('electronics', 'Electronics'),
        ('furniture', 'Furniture'),
        ('clothing', 'Clothing'),
    ]

    purchase = models.ForeignKey(Purchase, related_name='items', on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    item_type = models.CharField(max_length=50, choices=ITEM_TYPES)
    purchase_date = models.DateField()
    stock_available = models.BooleanField(default=False)

    def __str__(self):
        return self.item_name

