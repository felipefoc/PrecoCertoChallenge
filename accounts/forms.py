from django import forms
from accounts.models import CustomUser
from django.contrib.auth.forms import UserCreationForm



class UserRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'company')

