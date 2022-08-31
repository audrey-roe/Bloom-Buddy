from django.shortcuts import render, redirect
from .serializer import appointmentSerializer
from .models import appointment
from django.http import HttpResponse
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.



class book_appointment(APIView):
    def post(self, request):
        serializer = appointmentSerializer(request.data, many=True)
        if serializer.is_valid():
            # This part is not meant to save directly untill payment has been made ,payment part pending
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            messages.success(request, ('Your appointment was successfully added!'))
            
		   
      
      
        else:
            messages.error(request, 'Error saving form')
            
            
        
        
	   
        
            
    	
		
    def get(self,request):
        appointment_page = appointmentSerializer()
        appointments = appointment.objects.all()  #use this if doctor wants to check appointments
        return Response(request, context={'appointments':appointments})
	 
	    
        
	
        


        
