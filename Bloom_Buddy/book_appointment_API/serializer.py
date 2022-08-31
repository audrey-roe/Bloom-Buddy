
from .models import appointment
from rest_framework import serializers

class appointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = appointment
        fields = ('appointment_month', 'appointment_date', 'appointment_time', 'full_name', 'age', 'gender')