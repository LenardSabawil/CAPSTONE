from django.shortcuts import render, redirect
from .models import invoice
from django.http import HttpResponse
from dashboard.models import Order

# Create your views here.
def generate_bill(request, pk):
    try:
        order = Order.objects.get(id=pk)
        product = order.product

        if product is None:
            return render(request, 'invoice/error.html', {'error_message': 'Product not found'})

        product_name = product.name
        order_quantity = order.order_quantity
        product_price = product.price

        if product_price is None:
            return render(request, 'invoice/error.html', {'error_message': 'Product price not available'})

        total_amount = product_price * order_quantity

        if request.method == 'POST':
            try:
                bill = invoice.objects.get(order=order)
                room = bill.room
                booking = bill.booking
                user = order.staff
                user_info = f"Ordered by: {user.username} (Email: {user.email})"

                context = {
                    'order': order,
                    'product_name': product_name,
                    'order_quantity': order_quantity,
                    'product_price': product_price,
                    'total_amount': total_amount,
                    'room_info': f"Room: {room}\nBooking Info: {booking}",
                    'user_info': user_info,
                }

                return render(request, 'invoice/bill.html', context)
            except invoice.DoesNotExist:
                return render(request, 'invoice/error.html', {'error_message': 'Invoice not found'})
    except Order.DoesNotExist:
        return render(request, 'invoice/error.html', {'error_message': 'Order not found'})

    # If none of the conditions match, return a generic error response.
    return render(request, 'invoice/error.html', {'error_message': 'An error occurred while generating the bill'})