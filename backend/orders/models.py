from django.db import models
from menu.models import Menu

# Create your models here.
class Order(models.Model):
    reference = models.CharField(max_length=12)
    customer = models.CharField(max_length=20)
    paid = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField(
        Menu, through='OrderItem', related_name='items'
        )
    
    def __str__(self):
        return self.reference

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order')
    item = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_item')
    quantity = models.IntegerField()