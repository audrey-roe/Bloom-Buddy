from django import forms
from .models import appointment

class appointmentForm(forms.ModelForm):

    class Meta:
        model = appointment
        fields = ('appointment_month', 'appointment_date', 'appointment_time', 'full_name', 'age', 'gender')