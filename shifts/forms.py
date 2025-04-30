from django import forms
from .models import ShiftRequest

class ShiftRequestForm(forms.ModelForm):
    class Meta:
        model = ShiftRequest
        fields = ['start_datetime', 'bonus', 'extra_info']
        widgets = {
            'start_datetime': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control',  # Optional, for styling
                'placeholder': 'Choose date and time',
            }),
            'bonus': forms.NumberInput(attrs={'class': 'form-control'}),
            'extra_info': forms.Textarea(attrs={'class': 'form-control'}),
        }
        # Optional: format if needed — in many cases this line is not required,
        # Django will handle the datetime-local format automatically.
        # But if you see format issues, uncomment the following:
        
        input_formats = {'start_datetime': ['%Y-%m-%dT%H:%M']}