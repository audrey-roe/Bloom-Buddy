from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .serializers import *
from django.contrib import messages
from django.contrib.auth import authenticate, login as loginUser, update_session_auth_hash
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
import io
# from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.urls import reverse
import json
from time import time
from django.views.decorators.csrf import csrf_exempt
from Bloom_Buddy.settings import *



import paystack #test with sandbox
client = paystack.Client(auth=('KEY_ID', 'KEY_SECRET'))

# Create your views here.


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
    context = { 'allposts':allposts, 
                'main_course':main_course, 
                'top_three_catg':top_three_catg, 
                'catg':catg, 
                'slider_post':slider_post, 
                'latest_catg':latest_catg, 
                'latest_post':latest_post, 
                'totalposts':totalposts, 
                # 'catg_parent':catg_parent,
                'allcat':allcat, 
                'categories':categories, 
                'footcategories':footcategories, 
                'rev':rev, 
                'latest_catg_all':latest_catg_all
                }
    return render(request, 'home.html', context)


def totalposts(request):
    total = Post.objects.all()
    context = {'total':total}
    return render(request, 'total.html', context)

def post_by_category(request, catslug):
    posts = Post.objects.all()
    cat_post = Post.objects.filter(category__slug=catslug)
    allposts = Post.objects.all().filter(maincourse=True)
    slider_post = Post.objects.all().filter(slider_post=True)
    top_three_catg = Category.objects.filter(top_three_cat=True)[:3]
    main_course = MainCourse.objects.all()
    allcat = Category.objects.all()
    categories = Category.objects.filter(parent=None).order_by('-created_at')[:7]
    footcategories = Category.objects.filter(parent=None)[:2]
    catg = Category.objects.all().exclude(parent=None).order_by('-created_at')[:7]
    catg_parent = Category.objects.all().exclude(parent=True)
    latest_catg = Category.objects.filter(parent=None)[:5]
    latest_post = Post.objects.order_by('-date')[:4]
    latest_catg_all = Category.objects.filter(parent=None)[5:]
    rev = Reviews.objects.all().order_by('-created')[:6]
    context = {'latest_catg_all':latest_catg_all, 'rev':rev, 'posts':posts, 'cat_post':cat_post,'allposts':allposts, 'main_course':main_course, 'top_three_catg':top_three_catg, 'catg':catg, 'slider_post':slider_post, 'latest_catg':latest_catg, 'latest_post':latest_post}
    return render(request, 'postbycat.html', context)

def allpost_by_category(request, postslug):
    posts = Post.objects.all()
    cat_post = Post.objects.filter(category__slug=postslug)
    subcat_post = Post.objects.filter(subcategory__slug=postslug)
    allposts = Post.objects.all().filter(maincourse=True)
    allcat = Category.objects.all()
    context = {'posts':posts,'subcat_post':subcat_post, 'cat_post':cat_post,'allposts':allposts,'allcat':allcat,}
    return render(request, 'allpostsbycat.html', context)

def subcat_by_category(request, subcatslug):
    allcats = get_object_or_404(Category, slug=subcatslug)
    category = subcat.objects.filter(slug=subcatslug)
    # allsubcatg = allcats.subcat.filter(parent__slug=slug)
    cat_subcat = subcat.objects.filter(parent__slug=subcatslug)
    context = {'cat_subcat':cat_subcat, 'category':category, 'allcats':allcats}
    return render(request, 'subcatbyhtml.html', context)
  
def post_details(request, category_slug, slug):
    posts = Post.objects.filter(slug=slug).first()
    category = Post.objects.filter(slug=category_slug)
    catg_parent = Category.objects.all().exclude(parent=True)    
    allcat = Category.objects.all()
    allpost = get_object_or_404(Post, slug=slug)
    time = timing.objects.filter(Post=allpost)    
    #for Videos
    vid = video.objects.filter(post=allpost)    
    #for Reviews
    if request.method == 'POST' and request.user.is_authenticated:
        allstars = request.POST.get('stars', '')
        allcontent = request.POST.get('content', '')
        reviews = Reviews.objects.create(post=allpost, user=request.user, stars=allstars, content=allcontent)
        return redirect('home')        
    reviews = Reviews.objects.filter(post=allpost)    

    context = {'posts':posts, 'category':category, 'allcat':allcat, 'catg_parent':catg_parent, 'allpost':allpost, 'reviews':reviews, 'time':time, 'videos':vid}
    return render(request, 'details.html', context)

def search(request):
    search = request.GET['search']
    totalposts = Post.objects.filter(title__icontains=search)
    context = {'totalposts':totalposts, 'search':search}
    return render(request, 'search.html', context)

def videos(request):
    return render(request, 'videos.html')

def addVideosWatched(request, video_id):
    pass

def courses(request):
    main_course = MainCourse.objects.all()
    context = {'main_course':main_course}
    return render(request, 'courses.html', context)

@csrf_exempt
def verify_payment(request):
    if request.method == 'POST':
        data = request.POST
        context = {}
        print(data)
        try:
            client.utility.verify_payment_signature(data)
            paystack_order_id = data['paystack_order_id']
            paystack_payment_id = data['paystack_payment_id']
            order = Order.objects.get(order_id = paystack_order_id)
            order.payment_id = paystack_payment_id
            order.ordered = True
            order.save() # i remembered the save this time
            cart_items = Cart.objects.filter(user=request.user, purchase=False)
            for item in cart_items:
                item.purchase = True
                item.save()
            return redirect('home')
        except:
            return HttpResponse("Invalid Payment Details")    


def add_videos(request):
    video= videoserial()
    if request.method=='POST':
        video=videoserial(request.POST, request.FILES)
        if video.is_valid():
            video.save()
        messages.success(request, "video Added Sucessfully !!")    
        return redirect('home')
    return render(request, "webadmin/addvideo.html", {'video':video})

def edit_videos(request, id):
    if request.method == 'POST':
        vid = video.objects.get(id=id)
        editvideoForm= videoserial(request.POST or None, request.FILES or None, instance=vid)
        if editvideoForm.is_valid():
            editvideoForm.save()
        messages.success(request, "Video Update Sucessfully !!")
        return redirect('allcat')
    else:
        vid = video.objects.get(id=id)
        editvideoForm= videoserial(instance=vid)

    return render(request, "webadmin/editvideo.html", {'editvideo':editvideoForm})

def delete_video(request, id):
    delete = video.objects.get(pk=id)  #pk means primary key
    delete.delete()
    messages.success(request, "video Deleted Successfully.")
    return redirect('allcourses')   

def allvideos(request):
    vid = video.objects.all()
    context = {'video':vid}
    return render(request, 'webadmin/allvideo.html', context)

def paid_video(request, slug):
    allpost = get_object_or_404(Post, slug=slug)
    vid = video.objects.filter(post=allpost)
    context = {'allpost':allpost, 'vid':vid}
    return render(request, 'users/video.html', context)
