from django.contrib.auth.models import User
from .models import Order
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Order)
def update_quantity(sender, instance, created, **kwargs):
    instance.product.quantity -= instance.order_quantity
    instance.product.save()
