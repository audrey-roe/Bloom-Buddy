from pyexpat.errors import messages
from django.contrib.auth.models import Group, User
from django.core.exceptions import ValidationError
from .models import *
from rest_framework import serializers


class Postserial(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'



class timingserial(serializers.ModelSerializer):
    class Meta:
        model = timing
        fields =  '__all__'

class Catserial(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class Maincourseserial(serializers.ModelSerializer):
    
    class Meta:
        model = MainCourse
        fields = '__all__'


# User Creation
# class CustomerAuthserial(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         fields = '__all__'

class Customerserial(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields='__all__'

class videoserial(serializers.ModelSerializer):

    class Meta:
        model = video
        fields = '__all__'

class subcatgserial(serializers.ModelSerializer):
    
    class Meta:
        model = subcat
        fields = '__all__'
     

class reviewserial(serializers.ModelSerializer):

    class Meta:
        model = Reviews
        fields = '__all__'          

class checkoutserial(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'      

class CartSerial(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__' 
           

class OrderSerializer(serializers.ModelSerializer):
        class Meta:
             model = Order
             fields = '__all__' 

# class sendmsgserialize(serializers.ModelSerializer):

#     class Meta:
#         model = message
#         fields = '__all__'