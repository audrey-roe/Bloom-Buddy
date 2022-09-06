from rest_framework import serializers

from django.contrib.auth.forms import UserCreationForm

from .models import *

class createuserserial(serializers.ModelSerializer):
    class Meta:
        model=info
        fields="__all__"
 
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Question
        fields="__all__"