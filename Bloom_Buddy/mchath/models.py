from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class customer(models.Model):
    caregiver_name = models.CharField(max_length= 200)
    child_age = models.PositiveIntegerField()
    child_name = models.CharField(max_length= 200)
    relation_to_child = models.CharField(max_length= 200)
    caregiver_email = models.EmailField( max_length=50)
    caregiver_phone = models.BigIntegerField()
    date = models.DateField(auto_now_add=True, null=True)
    score = models.IntegerField()
    USERNAME_FIELD = 'username'


    def __str__(self):
        return self.caregiver_name


class quiz(models.Model):
    question = models.CharField(max_length=200, null=True)
    op1 = models.CharField(max_length=200, null=True)
    op2 = models.CharField(max_length=200, null=True)
    ans = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return f"Question: {self.question} Ans: {self.ans}"
