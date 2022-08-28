from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login as loginUser, update_session_auth_hash
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
import io
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.urls import reverse
import json
from time import time
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from Bloom_Buddy.settings import *

# import paymentgateway

# parse auth keyid and keysecret into client eg, client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))

def home(request):
    allposts = Post.objects.all().filter(maincourse=True)
    totalposts = Post.objects.all().order_by('-date')[:8]
    slider_post = Post.objects.all().filter(slider_post=True)
    top_three_catg = Category.objects.filter(top_three_cat=True)[:3]
    main_course = MainCourse.objects.all()
    allcat = Category.objects.all()
    categories = Category.objects.all().filter(top_three_cat=False).filter(more=False).order_by('-created_at')[:7]
    footcategories = Category.objects.filter(parent=None)[:2]
    catg = Category.objects.all().exclude(parent=None).order_by('-created_at')[:7]
    # catg_parent = Category.objects.all().exclude(parent=True).order_by('-hit')
    latest_catg = Category.objects.filter(parent=None)[:5]
    latest_catg_all = Category.objects.filter(parent=None)[5:]
    latest_post = Post.objects.order_by('-date')[:4]
    rev = Reviews.objects.all().order_by('-created')[:6]
    context = {'allposts':allposts, 'main_course':main_course, 'top_three_catg':top_three_catg, 'catg':catg, 'slider_post':slider_post, 'latest_catg':latest_catg, 'latest_post':latest_post, 'totalposts':totalposts, 
    
    # 'catg_parent':catg_parent,
     'allcat':allcat, 'categories':categories, 'footcategories':footcategories, 'rev':rev, 'latest_catg_all':latest_catg_all}
    return render(request,