from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class info(models.Model):
    caregiver = models.OneToOneField(User, on_delete=models.CASCADE)#should contain name and email
    child_name = models.CharField(max_length=200)
    child_age = models.PositiveIntegerField()
    relation_to_child = models.CharField(max_length= 200)
    caregiver_email = models.EmailField( max_length=50)
    caregiver_phone = models.BigIntegerField()
    date = models.DateField(null=True, blank=True)
    test_score = models.IntegerField(null = True, blank= True)


    def __str__(self):
        return self.child_name


class test(models.Model):
    question = models.CharField(max_length=200,null=True)
    ans = models.BooleanField(max_length=200, null=True)
    
    def __str__(self):
        return f"Question: {self.question} Ans: {self.ans}"