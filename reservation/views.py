from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room, Booking
from .forms import AvailabilityForm
from reservation.booking_functions.availability import check_availability
from django.core.mail import send_mail
from django.contrib import messages


def room_list(request):
    room = Room.objects.all()
    return render(request, 'reservation/room_list.html', {'room': room})


def booking_view(request):
    if request.method == 'POST':
        form = AvailabilityForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            room_list = Room.objects.filter(category=data['room_category'])
            available_rooms = []

            for room in room_list:
                if check_availability(room, data['check_in'], data['check_out']):
                    available_rooms.append(room)

            if len(available_rooms) > 0:
                room = available_rooms[0]
                booking = Booking.objects.create(
                    user=request.user,
                    room=room,
                    check_in=data['check_in'],
                    check_out=data['check_out'],
                )
                booking.save()
                return HttpResponse(booking)
            else:
                return HttpResponse('All of This Category of Rooms is Booked!!! Try another one')
    else:
        form = AvailabilityForm()

    return render(request, 'reservation/availability_form.html', {'form': form})


def approve_booking(request, booking_id):
    booking = Booking.objects.all(Booking, pk=booking_id)
    
    if not booking.is_approved:
        booking.is_approved = True
        booking.save()
        
        # Send a confirmation email to the customer
        subject = 'Booking Confirmation'
        message = f'Your booking for room {booking.room} from {booking.check_in} to {booking.check_out} has been approved.'
        from_email = 'your_email@gmail.com'  # Replace with your email address
        recipient_list = [booking.user.email]  # Assuming you have an email field in your User model
        
        try:
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            messages.success(request, 'Booking approved, and a confirmation email has been sent to the customer.')
        except Exception as e:
            messages.error(request, 'An error occurred while sending the confirmation email.')
    
    return redirect('booking-list')  # Redirect to a page showing all booking requests