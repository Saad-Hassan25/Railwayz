from django import forms
from .models import Passenger

class PassengerRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Passenger
        fields = ['firstName', 'lastName', 'email', 'password', 'address', 'cnic', 'phoneNumber', 'gender']

class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
