from django.contrib.auth import get_user_model
from django.db import models
# Create your models here.
User = get_user_model()
class membership (models.Model):
   name = models.CharField(max_length=50, default='Free')
   price = models.FloatField( default='0')
   user = models.OneToOneField (User, on_delete=models.CASCADE, related_name="user")

   def __str__(self):
        return self.name

   