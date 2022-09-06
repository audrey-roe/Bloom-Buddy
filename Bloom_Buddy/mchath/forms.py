from django.forms import ModelForm
from django import forms
from .models import customer, quiz
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class createcustomerform(UserCreationForm):
    caregiver_name = forms.CharField()
    child_age = forms.IntegerField()
    child_name = forms.CharField()
    relation_to_child = forms.CharField()
    caregiver_email = forms.EmailField()
    caregiver_phone = forms.IntegerField()
    # date = forms.DateTimeField()
    # USERNAME_FIELD = 'username'
    class Meta:
        model=customer
        fields=['caregiver_name', 'child_age', 'child_name', 'relation_to_child', 'caregiver_email', 'caregiver_phone' ]

class quizform(ModelForm):
    class Meta:
        model=quiz
        fields="__all__"