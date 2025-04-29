from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CompanySignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'company'  # force user type to 'company'
        if commit:
            user.save()
        return user
