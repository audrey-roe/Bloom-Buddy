from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class createuserform(UserCreationForm):
    class Meta:
        model=setup
        fields=['caregiver_name', 'child_age', 'child_name', 'relation_to_child', 'caregiver_email', 'caregiver_phone', 'date' ]

class quizform(ModelForm):
    class Meta:
        model=quiz
        fields="__all__"