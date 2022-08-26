from django.shortcuts import render, redirect
from django.views import View
from .models import appointment
from .forms import appointmentForm
from django.contrib import messages

# Create your views here.



class book_appointment(View):
    def post(self, request):
        appointment_form = appointmentForm(request.POST)
        if appointment_form.is_valid():
            appointment_form.save()
            messages.success(request, ('Your appointment was successfully added!'))
            
		   
      
      
        else:
            messages.error(request, 'Error saving form')
            
            
        return redirect("appointment")
            
        
        
	   
        
            
       
        
         
         
         
			
		
			
		
		
		
    def get(self,request):
        appointment_form = appointmentForm()
        return render(request=request, template_name="appointment.html", context={'appointment_form':appointment_form, 'appointments':appointments})
	    # appointments = appointment.objects.all()  use this if doctor wants to check appointments
	    
        
	
        


        
