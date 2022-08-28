from django.shortcuts import render, redirect,get_object_or_404
from django.http.request import HttpRequest
from django.http.response import HttpResponse 
from django.conf import settings
from .models import Payment
from . import forms
from .forms import PaymentForm
import  requests
from django.contrib import messages


# Create your views here.

def initiate_payment(request: HttpRequest)->HttpResponse:
    if request.method == 'POST':
        payment_form = forms.PaymentForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save() 
            return  render (request, 'make_payment.html',{'payment':payment})
        
        
    else:
        payment_form = forms.PaymentForm()
        
    return render(request, 'initiate_payment.html',{'payment_form':payment_form})
        
        

def verify_payment(request: HttpRequest,ref:str):
    payment = get_object_or_404(Payment, ref=ref)
    verified  = payment.verify_payment()
    if verified:
        messages.success(request, "Verification succesfull")
    else:
        messages.error(request, "Verification failed ")
    return redirect('initiate-payment')

    
    
            
    
