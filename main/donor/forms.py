from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    contact = forms.CharField(max_length=20)
    address = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'contact', 'address', 'password1', 'password2']
