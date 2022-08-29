from pyexpat.errors import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import Group, User
from django.core.exceptions import ValidationError
from .models import *
from rest_framework import serializers


class Postserial(serializers.ModelSerializer):
    maincourse = serializers.ModelMultipleChoiceField(
            queryset=MainCourse.objects.all(),
            widget=serializers.CheckboxSelectMultiple,
            required=True)
    
    class Meta:
        model = Post
        fields = '__all__'

class EditPostserial(serializers.ModelSerializers):
    maincourse = serializers.ModelMultipleChoiceField(
            queryset=MainCourse.objects.all(),
            widget=serializers.CheckboxSelectMultiple,
            required=True)    
    class Meta:
        model = Post
        fields = '__all__'

class timingserial(serializers.ModelSerializers):
    class Meta:
        model = timing
        fields =  '__all__'

class Catserial(serializers.ModelSerializers):
    
    class Meta:
        model = Category
        fields = '__all__'

class EditCatserial(serializers.ModelSerializers):
    
    class Meta:
        model = Category
        fields = '__all__'

class Maincourseserial(serializers.ModelSerializers):
    
    class Meta:
        model = MainCourse
        fields = ['title']

class EditMaincourseserial(serializers.ModelSerializers):
    
    class Meta:
        model = MainCourse
        fields = ['title']


# User Creation
class CustomerAuthserial(serializers.ModelSerializers):
    username = serializers.EmailField(required=True , label="Email")

class CustomerCreationserial(serializers.ModelSerializers):
    
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

class Customerserial(serializers.ModelSerializers):
    class Meta:
        model=Customer
        fields=['address','mobile','profile_pic']

class CustomerEditserial(serializers.ModelSerializers):
    class Meta:
        model=Customer
        fields='__all__'

class CustomerCreationEditserial(serializers.ModelSerializers):
    # password = forms.CharField(widget=forms.TextInput(attrs={'type':'hidden'}))
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
    password = serializers.PasswordInput()


class Userpermission(serializers.ModelSerializer):
    role = serializers.ModelChoiceField(queryset=Group.objects.all())    

    class Meta:
        model = User
        fields = ['first_name','last_name']

class videoserial(serializers.ModelSerializers):

    class Meta:
        model = video
        fields = '__all__'


    
class leftmenu(serializers.ModelSerializers):
    class Meta:
        model = Category
        exclude = ['top_three_cat', 'more']    

class middlemenu(serializers.ModelSerializers):
    class Meta:
        model = Category
        exclude = ['parent', 'top_three_cat', 'logo1', 'logo2']    

class rightmenu(serializers.ModelSerializers):
    class Meta:
        model = Category
        exclude = ['parent', 'more', 'logo1', 'logo2']    

class admin_reviewsform(serializers.ModelSerializer):

    class Meta:
        model = Reviews
        fields = '__all__'          

class checkoutserial(serializers.ModelSerializer):
    #dunno what paystack will require

    mobile = serializers.IntegerField()        
    street_address = serializers.CharField()        
    apartment_address = serializers.CharField(required=False)
    country = serializers.CharField(label="Country")
    zipcode = serializers.CharField()
    same_billing_address = serializers.BooleanField(widget=serializers.CheckboxInput())
    save_info = serializers.BooleanField(widget=serializers.CheckboxInput())
    payment_option = serializers.BooleanField(widget=serializers.RadioSelect())         

# class sendmessage(forms.ModelForm):

#     class Meta:
#         model = message
#         fields = '__all__'
#         exclude = ['wp']
