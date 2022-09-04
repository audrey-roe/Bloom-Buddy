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
        fields = ['title']


# User Creation
class CustomerAuthserial(serializers.ModelSerializer):
    username = serializers.EmailField(required=True , label="Email")

class CustomerCreationserial(serializers.ModelSerializer):
    
    username = serializers.EmailField(required=True , label="Email" )
    first_name = serializers.CharField(required=True , label="First Name")
    last_name = serializers.CharField(required=True , label="Last Name")
    class Meta:
        model = User
        fields = ['username' ,'first_name' , "last_name" ]

    def clean_first_name(self):
        value = self.cleaned_data.get('first_name')
        if len(value.strip()) < 4 :
            raise ValidationError("First Name must be atleast 4 char long...")
        return value.strip()
    
    def clean_last_name(self):
        value = self.cleaned_data.get('last_name')
        if len(value.strip()) < 4 :
            raise ValidationError("Last Name must be atleast 4 char long...")
        return value.strip()

class Customerserial(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=['address','mobile','profile_pic']

class CustomerEditserial(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields='__all__'

class CustomerCreationEditserial(serializers.ModelSerializer):
    username = serializers.EmailField(required=True , label="Email" )
    first_name = serializers.CharField(required=True , label="First Name")
    last_name = serializers.CharField(required=True , label="Last Name")
    class Meta:
        model = User
        fields = ['username' ,'first_name' , "last_name"]
        exclude = ['password']

class changepassword(serializers.ModelSerializer):    
    class Meta:
        model = User
        fields = ['password1']
        exclude = ['username', 'first_name','last_name']

class Customerloginserial(serializers.ModelSerializer):
    username = serializers.EmailField(required=True, label="Email")
    password = serializers.CharField()


class Userpermission(serializers.ModelSerializer):
    # role = serializers.ModelChoiceField(queryset=Group.objects.all())    This part throws an error please check

    class Meta:
        model = User
        fields = ['first_name','last_name']

class videoserial(serializers.ModelSerializer):

    class Meta:
        model = video
        fields = '__all__'

class subcatg(serializers.ModelSerializer):
    
    class Meta:
        model = subcat
        fields = '__all__'
    
class leftmenu(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ['top_three_cat']    

class middlemenu(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ['parent', 'top_three_cat', ]    

class rightmenu(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ['parent']    

class reviewserial(serializers.ModelSerializer):

    class Meta:
        model = Reviews
        fields = '__all__'          

class checkoutserial(serializers.ModelSerializer):
    #dunno what paystack will require, just trying to be extensive

    mobile = serializers.IntegerField()        
    street_address = serializers.CharField()        
    state = serializers.CharField(required=False)
    country = serializers.CharField(label="Country")
    # zipcode = serializers.CharField()
    # billing_address = serializers.BooleanField(widget=serializers.CheckboxInput())   please check here an error is beign thrown
    # save_info = serializers.BooleanField(widget=serializers.CheckboxInput()) 
    # payment_option = serializers.BooleanField(widget=serializers.RadioSelect())  
    
    
class CartSeraializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__' 
           

class OrderSerializer(serializers.ModelSerializer):
        class Meta:
             model = Order
             fields = '__all__' 
             
             
    
    
# class sendmessage(forms.ModelForm):

#     class Meta:
#         model = message
#         fields = '__all__'
#         exclude = ['wp']
