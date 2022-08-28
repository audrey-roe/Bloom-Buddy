from .models import Payment
from django import forms


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ( "amount", "email",)
        


