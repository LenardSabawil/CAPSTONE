from django.db import models
from django.conf import settings


# Create your models here.

class Room(models.Model):
    ROOM_CATEGORIES = (
        ('YAC', 'AC'),
        ('NAC', 'NON-AC'),
        ('DEL', 'DELUXE'),
        ('KIN', 'KING'),
        ('QUE', 'QUEEN'),
    )
    number = models.IntegerField()
    category = models.CharField(max_length=3, choices=ROOM_CATEGORIES)
    beds = models.IntegerField()
    capacity = models.IntegerField()
    price = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.number}. {self.category} with {self.beds} beds for {self.capacity} people'


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    status = models.CharField(max_length=250, default="Pending")
    remarks = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f'{self.user} has booked {self.room} from {self.check_in} to {self.check_out}'
    


