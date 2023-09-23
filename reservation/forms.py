from django import forms
from django.forms.widgets import DateTimeInput

class AvailabilityForm(forms.Form):
    ROOM_CATEGORIES = (
        ('YAC', 'AC'),
        ('NAC', 'NON-AC'),
        ('DEL', 'DELUXE'),
        ('KIN', 'KING'),
        ('QUE', 'QUEEN'),
    )
    room_category = forms.ChoiceField(choices=ROOM_CATEGORIES, required=True)
    check_in = forms.DateTimeField(
        required=True,
        input_formats=["%Y-%m-%dT%h:%M"],
        widget=DateTimeInput(attrs={'type': 'datetime-local'}),
    )
    check_out = forms.DateTimeField(
        required=True,
        input_formats=["%Y-%m-%dT%h:%M"],
        widget=DateTimeInput(attrs={'type': 'datetime-local'}),
    )
