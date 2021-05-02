from django import forms
from django.contrib.auth.models import User
from accounts.models import Profile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'company')