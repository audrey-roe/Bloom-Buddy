from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class info(models.Model):
    childname = models.OneToOneField(User, max_length= 200, null =  False, blank = False, on_delete=models.CASCADE)
    childage = models.PositiveIntegerField()
    caregivername = models.CharField(max_length= 200, null =  False, blank = False)
    relationtochild = models.CharField(max_length= 200, null =  False, blank = False)
    caregiveremail = models.EmailField( max_length=50, db_index=True, unique=True)
    caregiverphone = models.BigIntegerField()
    date = models.DateField(null=True, blank=True)


    def __str__(self):
        return self.childname


class test(models.Model):
    question = models.CharField(max_length=200,null=True)
    yes = models.TextField(max_length= 3, null =  False, blank = False, default='Yes')
    no = models.TextField(max_length= 3, null =  False, blank = False, default='No')
    # op3 = models.CharField(max_length=200,null=True)
    # op4 = models.CharField(max_length=200,null=True)
    ans = models.BooleanField(max_length=200,null=True)

    def __str__(self):
        return self.question