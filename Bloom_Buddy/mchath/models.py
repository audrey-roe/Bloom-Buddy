from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class setup(models.Model):
    caregiver_name = models.CharField(max_length= 200, null =  False, blank = False)
    child_age = models.PositiveIntegerField()
    child_name = models.CharField(max_length= 200, null =  False, blank = False)
    relation_to_child = models.CharField(max_length= 200, null =  False, blank = False)
    caregiver_email = models.EmailField( max_length=50, db_index=True, unique=True)
    caregiver_phone = models.BigIntegerField()
    date = models.DateField(null=True, blank=True)
    score = models.IntegerField(null = True, blank= True)
    USERNAME_FIELD = 'username'


    def __str__(self):
        return self.childname


class quiz(models.Model):
    question = models.CharField(max_length=200,null=True)
    yes = models.TextField(max_length= 3, null =  False, blank = False, default='Yes')
    no = models.TextField(max_length= 3, null =  False, blank = False, default='No')
    # op3 = models.CharField(max_length=200,null=True)
    # op4 = models.CharField(max_length=200,null=True)
    ans = models.BooleanField(max_length=200,null=True)

    def __str__(self):
        return self.question