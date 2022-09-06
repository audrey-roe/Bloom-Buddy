from django.db import models

# Create your models here.

class info(models.Model):
    child_name = models.CharField(max_length= 200, null =  False, blank = False)
    child_age = models.PositiveIntegerField()
    caregiver_name = models.CharField(max_length= 200, null =  False, blank = False)
    relation_to_child = models.CharField(max_length= 200, null =  False, blank = False)
    caregiver_email = models.EmailField( max_length=50, db_index=True, unique=True)
    caregiver_phone = models.BigIntegerField()
    date = models.DateField(null=True, blank=True)


    def __str__(self):
        return self.child_name


class Question(models.Model):
    question = models.CharField(max_length=200,null=True)
    yes = models.TextField(max_length= 3, null =  True, blank = True)
    no = models.TextField(max_length= 3, null =  True, blank = True)
    
    
    
    
    
    def __str__(self):
        return self.question