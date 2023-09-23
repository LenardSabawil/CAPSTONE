from django.contrib import admin
from .models import Room, Booking

# Register your models here.
class RoomAdmin(admin.ModelAdmin):
    list_display = ('number', 'category', 'beds', 'capacity')
    list_filter = ['category']

admin.site.register(Room, RoomAdmin),
admin.site.register(Booking),
