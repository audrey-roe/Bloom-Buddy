from django.db import models

# Create your models here.
class appointment(models.Model):
    appointment_month = models.CharField(max_length=15)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=6)
    
    def __str__(self):
        return self.full_name +"'s Appointment"