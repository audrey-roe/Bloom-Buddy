from django.contrib import messages
from django.db import models
from auth_api.models import User, user_info_extend
from betarate_api import settings
# Create your models here.

# class realEstate_PropType(models.Model):
#     message= models.CharField(max_length = 200)
#     name = models.CharField(max_length = 200)
#     updated_at=models.DateTimeField(auto_now_add=True)
#     created_at=models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name 
        
class realEstate_Purpose(models.Model):
    message= models.CharField(max_length = 200)
    name = models.CharField(max_length = 200)
    updated_at=models.DateTimeField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    

    def __str__(self):
        return self.name 

class ImageAttachment(models.Model):
    file = models.FileField(upload_to ='media/propertyGallery/')   

class realEstate_offer(models.Model):
    PER_YEAR = '/Year'
    PER_MONTH = '/Month'
    PER_WEEK = '/Week'
    PER_DAY = '/Day'
    PER_HOUR = '/Hour'

    APARTMENT = 'apartment'
    HOUSE = 'house'
    FLAT = 'flat'
    LAND = 'land'
    OFFICE = 'office'
    SHOP = 'shop'

    CHOICES = (
        (PER_YEAR, '/Year'),
        (PER_MONTH, '/Month'),
        (PER_WEEK, '/Week'),
        (PER_DAY, '/Day'),
        (PER_HOUR, '/Hour'),
    )
    PURPOSE = (
        (APARTMENT, 'apartment'),
        (HOUSE, 'house'),
        (FLAT, 'flat'),
        (LAND, 'land'),
        (OFFICE, 'office'),
        (SHOP, 'shop'),
    )
    service_provider = models.ForeignKey(user_info_extend, on_delete=models.CASCADE)#this is meant to identify which service proveiders handels a loan 

    location= models.CharField(max_length = 200)
    title = models.CharField(max_length = 200)
    # propImage = models.BinaryField()
    imagegallery = models.FileField(upload_to ='media/propertyGallery/', blank = True) #for the multiple gallery pictures of the property for rent
    imageuploader_profile = models.ForeignKey(user_info_extend, on_delete=models.CASCADE, null=True, blank=True, related_name='imageUpload')
    # imagegallery = models.ManyToManyField(ImageAttachment, blank=True) #for the multiple gallery pictures of the property being uploaded
    description = models.TextField()
    price = models.FloatField(null=True, blank=True, default=0)
    duration = models.CharField(max_length=20, choices=CHOICES)
    bedrooms = models.CharField(max_length=3)
    toilets = models.IntegerField()
    bathrooms = models.IntegerField()
    parking = models.IntegerField()
    location = models.CharField(max_length = 60)
    state = models.CharField(max_length=20)
    local_government = models.CharField(max_length=20,null=True)
    covered_area = models.DecimalField(max_digits=20,decimal_places=3,default=1)
    total_area = models.DecimalField(max_digits=20,decimal_places=3,default=1)
    furnished_type = models.CharField(max_length=3, default="yes")
    currency = models.CharField(max_length=1, default="N")
    financing = models.CharField(max_length=3, default="yes")
    purpose = models.CharField(max_length=20,blank=True)
    propertyType  = models.CharField(max_length=20)
    youtube_link =models.URLField(max_length=200, null=True)
    instagram_link = models.URLField(max_length=200, null=True)

    updated_at=models.DateTimeField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title 

    def save(self, *args, **kwargs):
        if self.service_provider.user_type != 'realtor' :
            raise messages.error('user not allowed')
        super().save(*args,**kwargs)

class realest_saves(models.Model):
    saver = models.ForeignKey(User, on_delete=models.CASCADE)
    property_liked = models.ForeignKey(realEstate_offer, on_delete = models.CASCADE)

