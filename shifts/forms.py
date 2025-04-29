from django import forms
from .models import ShiftRequest

class ShiftRequestForm(forms.ModelForm):
    class Meta:
        model = ShiftRequest
        fields = ['start_datetime', 'bonus', 'extra_info']
