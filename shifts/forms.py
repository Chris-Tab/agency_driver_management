from django import forms
from .models import ShiftRequest

class ShiftRequestForm(forms.ModelForm):
    class Meta:
        model = ShiftRequest
        fields = ['start_datetime', 'bonus', 'extra_info']
        widgets = {
            'start_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        input_formats = {
            'start_datetime': ['%Y-%m-%dT%H:%M'],  # format used by datetime-local input
        }
        