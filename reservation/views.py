from django.shortcuts import render
from django.http import HttpResponse
from .models import Room, Booking
from .forms import AvailabilityForm
from reservation.booking_functions.availability import check_availability

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
