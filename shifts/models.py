from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.exceptions import ValidationError

class ShiftRequest(models.Model):
    company = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'user_type': 'company'})
    start_datetime = models.DateTimeField()
    bonus = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    extra_info = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # Validate that the start_datetime is in the future
        if self.start_datetime <= timezone.now():
            raise ValidationError('Start date and time must be in the future.')

    def __str__(self):
        return f"Shift for {self.company.username} at {self.start_datetime}"
    

    
class ShiftRequest(models.Model):
    company = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'user_type': 'company'})
    start_datetime = models.DateTimeField()
    bonus = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    extra_info = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # 🔥 Add this line:
    assigned_driver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_shifts', limit_choices_to={'user_type': 'driver'})

    def clean(self):
        if self.start_datetime <= timezone.now():
            raise ValidationError('Start date and time must be in the future.')

    def __str__(self):
        return f"Shift for {self.company.username} at {self.start_datetime}"