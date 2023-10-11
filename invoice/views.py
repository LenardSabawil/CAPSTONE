from django.shortcuts import render, redirect
from .models import invoice
from dashboard.models import Order

# Create your views here.
def generate_bill(request, pk):
        order = Order.objects.get(id=pk)
        product = order.product
        product_name = product.name
        order_quantity = order.order_quantity
        product_price = product.price
        total_amount = product_price * order_quantity

        if request.method == 'POST':
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

            return redirect(request, 'invoice/bill.html', context)

        else:
            return render(request, 'invoice/error.html', {'error_message': 'Invoice not found'})
