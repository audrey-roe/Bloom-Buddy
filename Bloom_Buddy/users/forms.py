from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = NewUser
        fields = ["user_name", "email", "password1", "password2"]

Plans=(('free','FREE'),('premium','PREMIUM'),('bloom','BLOOM_BUDDY'))

class UpdateUserForm(forms.ModelForm):

    # membership= forms.ChoiceField(choices=Plans)



    class Meta:
        model = NewUser
        fields = ["membership"]
