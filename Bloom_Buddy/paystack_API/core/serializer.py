from .models import Payment
from rest_framework import serializers


class PaymentSerializer(serializers.Serializer):
    class Meta:
        model = Payment
        fields = ( "amount", "email")
        


