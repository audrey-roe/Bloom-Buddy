from django.urls import path
from . views import book_appointment


urlpatterns = [
    path('book_appointment',book_appointment.as_view(), name='book_appointment'),
    
    
]