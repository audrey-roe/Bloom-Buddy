from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
 
class createuserform(UserCreationForm):
    class Meta:
        model=info
        fields="__all__"
 
class testform(ModelForm):
    class Meta:
        model=test
        fields="__all__"