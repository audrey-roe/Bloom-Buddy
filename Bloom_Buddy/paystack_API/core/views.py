from django.shortcuts import render, redirect,get_object_or_404
from django.http.request import HttpRequest
from django.http.response import HttpResponse 
from django.conf import settings
from .models import Payment
from .serializer import PaymentSerializer
import  requests
from rest_framework.views import APIView
from django.contrib import messages


# Create your views here.
class initiate_payment(APIView):
    

    def post(self,request: HttpRequest)->HttpResponse:
        
        
        serializer = PaymentSerializer(request.data, many=True)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            messages.success(request, ('details received'))
            
            
    def get(self,request):
        
        return Response(request, context={'message':"page loaded  successfully"})
            
        
class verify_payment(APIView):
    
    def get(self,request: HttpRequest,ref:str):
        payment = get_object_or_404(Payment, ref=ref)
        verified  = payment.verify_payment()
        if verified:
            messages.success(request, "Verification succesfull")
            return Response(request, context={'message':"Verified successfully"} )
        else:
            messages.error(request, "Verification failed ")
        # return redirect('initiate-payment')




    
    
    
            
    
