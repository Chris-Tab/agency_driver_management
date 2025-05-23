from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('company', 'Company'),
        ('agency', 'Agency'),
        ('driver', 'Driver'),
    )

    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)