from django import forms
from django.utils import timezone
from .models import ShiftRequest
from .models import DriverHoliday

class ShiftRequestForm(forms.ModelForm):
    class Meta:
        model = ShiftRequest
        fields = ['start_datetime', 'bonus', 'extra_info']
        widgets = {
            'start_datetime': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control',
            }),
            'bonus': forms.NumberInput(attrs={'class': 'form-control'}),
            'extra_info': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Only set initial value if it's a new form (not editing an existing shift)
        if not self.instance.pk:
            now = timezone.now().replace(microsecond=0, second=0)
            self.fields['start_datetime'].initial = now.strftime('%Y-%m-%dT%H:%M')

class DriverHolidayForm(forms.ModelForm):
    class Meta:
        model = DriverHoliday
        fields = ['start_date', 'end_date', 'notes']
        widgets = {
            'start_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'end_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'notes': forms.Textarea(attrs={
                'rows': 2,
                'class': 'form-control'
            }),
        }

