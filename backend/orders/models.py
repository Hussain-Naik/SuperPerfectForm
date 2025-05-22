from django.db import models
from menu.models import Menu

# Create your models here.
class Order(models.Model):
    reference = models.CharField(max_length=12)
    customer = models.CharField(max_length=20)
    paid = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Menu, through='OrderItem')
    
    def __str__(self):
        return self.reference

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)