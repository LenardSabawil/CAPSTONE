from django.db import models
from django.contrib.auth.models import User
from dashboard.models import Product, Order
from reservation.models import Room, Booking

# Create your models here.

class invoice(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    
    def total_amount(self):
        return self.order.product.price * self.order.order_quantity

    def __str__(self):
        return f'Bill for {self.order.staff.username}'