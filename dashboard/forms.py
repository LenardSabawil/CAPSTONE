from django import forms
from .models import Product, Order



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'quantity']


class OrderForm(forms.ModelForm):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), label='Product')
    order_quantity = forms.IntegerField(label='Quantity')
    class Meta:
        model = Order
        fields = ['product', 'order_quantity']
