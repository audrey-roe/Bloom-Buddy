from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, redirect, render
from .serializers import *
from django.contrib import messages
from django.contrib.auth import authenticate, login as loginUser, update_session_auth_hash
from django.http import HttpResponse
from time import time
from django.views.decorators.csrf import csrf_exempt
from Bloom_Buddy.settings import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status



# import paystack #test with sandbox
# client = paystack.auth=('KEY_ID', 'KEY_SECRET')
# client = paystack.Client(auth=('KEY_ID', 'KEY_SECRET')) this does not work , says no attribute named Client

# Create your views here.

class home(APIView):
    def get(self, request):
        allposts = Postserial(Post.objects.filter(maincourse=True), many = True)
        totalposts = Postserial(Post.objects.order_by('-date')[:8], many = True)
        top_three_catg = Catserial(Category.objects.filter(top_three_cat=True)[:3], many = True)
        main_course = Maincourseserial(MainCourse.objects.all(), many = True)
        allcat = Catserial(Category.objects.all(), many = True)
        categories = Catserial(Category.objects.filter(top_three_cat=False).filter(more=False).order_by('-created_at')[:7], many = True)
        catg = Catserial(Category.objects.exclude(parent=None).order_by('-created_at')[:7], many = True)
        latest_catg = Catserial(Category.objects.filter(parent=None)[:5], many = True)
        latest_catg_all = Catserial(Category.objects.filter(parent=None)[5:], many = True)
        latest_post = Postserial(Post.objects.order_by('-date')[:4], many = True)
        rev = reviewserial(Reviews.objects.order_by('-created')[:6], many = True)
        context = { 'allposts':allposts, 
                    'main_course':main_course, 
                    'top_three_catg':top_three_catg, 
                    'catg':catg, 
                    'latest_catg':latest_catg, 
                    'latest_post':latest_post, 
                    'totalposts':totalposts, 
                    'allcat':allcat, 
                    'categories':categories, 
                    'latest_catg_all':latest_catg_all,
                    'reviews' : rev
                    }
        return Response(context,status=HTTP_200_OK)



def totalposts(request):
    total = Postserial(Post.objects.all(), many=True)
    context = {'total':total}
    # return render(request, 'total.html', context)
    return Response(context,status=HTTP_200_OK)

def post_by_category(request, catslug):
    posts = Postserial(Post.objects.all(), many=True)
    cat_post = Postserial(Post.objects.filter(category__slug=catslug), many=True)
    allposts = Postserial(Post.objects.filter(maincourse=True), many=True)
    slider_post = Postserial(Post.objects.filter(slider_post=True), many=True)
    top_three_catg = Catserial(Category.objects.filter(top_three_cat=True)[:3], many=True)
    main_course = Maincourseserial(MainCourse.objects.all(), many=True)
    allcat = Catserial(Category.objects.all(), many=True)
    categories = Catserial(Category.objects.filter(parent=None).order_by('-created_at')[:7], many=True)
    footcategories = Catserial(Category.objects.filter(parent=None)[:2], many=True)
    catg = Catserial(Category.objects.exclude(parent=None).order_by('-created_at')[:7], many=True)
    catg_parent = Catserial(Category.objects.exclude(parent=True), many=True)
    latest_catg = Catserial(Category.objects.filter(parent=None)[:5], many=True)
    latest_post = Postserial(Post.objects.order_by('-date')[:4], many=True)
    latest_catg_all = Catserial(Category.objects.filter(parent=None)[5:], many=True)
    rev = reviewserial(Reviews.objects.order_by('-created')[:6], many=True)
    context = {'latest_catg_all':latest_catg_all, 'rev':rev, 'posts':posts, 'cat_post':cat_post,'allposts':allposts, 'main_course':main_course, 'top_three_catg':top_three_catg, 'catg':catg, 'slider_post':slider_post, 'latest_catg':latest_catg, 'latest_post':latest_post}
    # return render(request, 'postbycat.html', context)
    return Response(context,status=HTTP_200_OK)

def allpost_by_category(request, postslug):
    posts = Postserial(Post.objects.all(), many=True)
    cat_post = Postserial(Post.objects.filter(category__slug=postslug), many=True)
    subcat_post = Postserial(Post.objects.filter(subcategory__slug=postslug), many=True)
    allposts = Postserial(Post.objects.filter(maincourse=True), many=True)
    allcat = Catserial(Category.objects.all(), many=True)
    context = {'posts':posts,'subcat_post':subcat_post, 'cat_post':cat_post,'allposts':allposts,'allcat':allcat,}
    return Response(context,status=HTTP_200_OK)

def subcat_by_category(request, subcatslug):
    allcats = Catserial(get_object_or_404(Category, slug=subcatslug), many=True)
    category = subcatg(subcat.objects.filter(slug=subcatslug), many=True)
    # allsubcatg = allcats.subcat.filter(parent__slug=slug)
    cat_subcat = subcatg(subcat.objects.filter(parent__slug=subcatslug), many=True)
    context = {'cat_subcat':cat_subcat, 'category':category, 'allcats':allcats}
    return Response(context,status=HTTP_200_OK)         
  
class post_details(APIView):
    def get(self, request, category_slug, slug):
        posts = Postserial(Post.objects.filter(slug=slug).first())
        category = Postserial(Post.objects.filter(slug=category_slug), many = True)
        catg_parent = Catserial(Category.objects.exclude(parent=True), many = True)
        allcat = Catserial(Category.objects.all(), many = True)
        allpost = Postserial(Post.objects.all(), many = True)
        time = timingserial(timing.objects.filter(Post=allpost), many = True)
        #for Videos
        vid = videoserial(video.objects.filter(post=allpost), many = True)
        #for Reviews
            
        reviews = reviewserial(Reviews.objects.filter(post=allpost), many = True)

        context = {'posts':posts, 'category':category, 'allcat':allcat, 'catg_parent':catg_parent, 'allpost':allpost, 'reviews':reviews, 'time':time, 'videos':vid}
        return Response (context, status=HTTP_200_OK)
    
    def post(self, request):
        Reviews.objects.create(post=Post.objects.get(
            id = request.data['rev_id']),
            user=request.user,
            stars=request.data['no_o_stars'],
            content=request.data['content']
            )
        return Response({
            'message' : 'successfully added review'
        })

def search(request):
    search = request.GET['search']
    totalposts = Postserial(Post.objects.filter(title__icontains=search), many=True)
    context = {'totalposts':totalposts, 'search':search}
    return Response(context, status=HTTP_200_OK)
    

def videos(request):
   return Response(status=HTTP_200_OK)

def addVideosWatched(request, video_id):
    pass

def courses(request):
    main_course = Maincourseserial(MainCourse.objects.all(), many=True)
    context = {'main_course':main_course}
    return Response(context, status=HTTP_200_OK)

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
            return Response(status=HTTP_200_OK)
        except:
            # return HttpResponse("Invalid Payment Details")
            return Response(status=HTTP_206_PARTIAL_CONTENT)   

def logout(request):
    request.session.clear()
    # return redirect('home')
    return Response(status=HTTP_200_OK)

def userdashboard(request):
    customer = Customerserial(Customer.objects.all(), many=True)
    carts = Catserial(Cart.objects.filter(user=request.user, purchase=True), many=True)
    orders = Order.objects.filter(user=request.user, ordered=True) # coming back to create a serializer
    context = {'carts':carts,'customer':customer, 'orders':orders}
    # return render(request, 'index.html', context)
    return Response(context, status=HTTP_200_OK)

def userprofile(request):
    customer = Customerserial(Customer.objects.get(user_id=request.user.id), many=True)
    context = {'customer':customer}
    # return render(request, 'users/profile.html', context)
    return Response(context, status=HTTP_200_OK)

def remove_from_cart(request, id):
    item = get_object_or_404(Post, id=id)
    order_obj = Order.objects.filter(user=request.user, ordered=False)
    if order_obj.exists():
        order = order_obj[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Cart.objects.filter(item=item, user=request.user, purchase=False)[0]
            order.orderitems.remove(order_item)
            order_item.delete()
            messages.warning(request, "This product is removed from your cart")
            # return redirect("cart")
            return Response(status=HTTP_200_OK)
            
        else:
            messages.info(request, "This item was not in your cart")
            # return redirect("cart")
            return Response(status=HTTP_204_NO_CONTENT)
            
    else:
        messages.info(request,"You don't have an active order")
        # return redirect("home")
        return Response(status=HTTP_204_NO_CONTENT)    
        



def checkout(request):
    user = None
    # coupon = promocode.objects.all()
    if request.method == 'get':
        try:
            orders = Order.objects.get(user=request.user, ordered=False)     # create an order serializer for this
            context = {'orders':orders}
            return Response(context, status=HTTP_200_OK)
        except ObjectDoesNotExist:
            messages.info(request, 'You do not have an active order')
            # return redirect('checkout')
            return Response(status=HTTP_204_NO_CONTENT)
    
    orders = Order.objects.filter(user=request.user, ordered=False)           
    user = request.user        
    if orders.exists():
        order = orders[0]   
    orderss = None    
    order_payment = None
    action = request.GET.get('action')    
    if action == 'create_payment':
        amount = int(order.get_totals() * 100)
        currency = "NGN"
        receipt = f"template-{int(time())}"
        notes = {
                "email": user.email,
                "name": f'{user.first_name} {user.last_name}'
        }
        orderss = client.order.create({
        'amount':amount,
        'currency':currency,
        'receipt':receipt,
        'notes':notes
        })

        orders = Order.objects.filter(user=request.user, ordered=False)    
        order_payment = orders[0]
        order_payment.user = user
        order_payment.emailAddress = user.email
        # order_payment.coupon = order.coupon
        order_payment.order_id = orderss.get('id')
        order_payment.total = orderss.get('amount')
        order_payment.save()
    context = {'orderss':orderss, 'order_payment':order_payment, 'orders':orders, 'order':order}
    return Response(context, status=HTTP_200_OK)


def webadmin(request):
    postcount = Post.objects.count()
    catcount = Category.objects.count()
    usercount = User.objects.count()
    orders = Order.objects.all()                                          # Create an order serializer and apply
    context = {'postcount':postcount, 'cat':catcount, 'user':usercount,"orders":orders}
    return Response(context, status=HTTP_200_OK)  

def add_post(request):
    posts= Postserial()
    context = {'post':posts}
    if request.method=='POST':
        posts=Postserial(request.POST, request.FILES)
        if posts.is_valid():
            posts.save()
        messages.success(request, "Posts Added Sucessfully !!")    
        # return redirect('allposts')
        return Response(status=HTTP_201_CREATED)
    return Response(context, status=HTTP_200_OK)


def add_course(request):
    course= Maincourseserial()
    context = {'course':course}
    if request.method=='POST':
        course=Maincourseserial(request.POST, request.FILES)
        if course.is_valid():
            course.save()
        messages.success(request, "Course Added Sucessfully !!")    
        # return redirect('allcourses')
        return Response(status=HTTP_201_CREATED)
        
    return Response(context,status=HTTP_200_OK)


def add_cat(request):
    category= Catserial()
    context = {'category':category}
    if request.method=='POST':
        category=Catserial(request.POST, request.FILES)
        if category.is_valid():
            category.save()
        messages.success(request, "category Added Sucessfully !!")    
        # return redirect('allcat')
        return Response(status=HTTP_201_CREATED)
    return Response(context,status=HTTP_200_OK)

def add_curriculam(request):
    category= Catserial()
    context = {'category':category}
    if request.method=='POST':
        category=Catserial(request.POST, request.FILES)
        if category.is_valid():
            category.save()
        messages.success(request, "category Added Sucessfully !!")    
        # return redirect('admin')
        return Response(status=HTTP_201_CREATED)
    return Response(context,status=HTTP_200_OK)

#This is for show all Posts in Custom Admin Panel
def allposts(request):
    posts = Postserial(Post.objects.all(), many=True)
    context = {'posts':posts}
    return Response(context,status=HTTP_200_OK)

#This is for show all Users in Custom Admin Panel
def allusers(request):
    # users = User.objects.all()
    customer =Customerserial(Customer.objects.all(), many=True)
    context = {
        # 'users':users
    'customer':customer
    }
    return Response(context,status=HTTP_200_OK)

def userdetails(request, id):
    customer = Customerserial(Customer.objects.filter(id=id).first(), many=True)
    context = {'customer':customer}
    return Response(context,status=HTTP_200_OK)

def allorders(request):
    orders = OrderSerialize(Order.objects.filter(ordered=True), many=True)                         #Created a serializer for order
    carts = CartSeraializer(Cart.objects.all(), many=True)                                         # Created a serializer for cart
    context = {
    'orders':orders, 'carts':carts,
    }
    return Response(context,status=HTTP_200_OK)


#This is for show all Categories in Custom Admin Panel
def allcat(request):
    cat = Catserial(Category.objects.filter(parent=None).order_by('hit'), many=True)
    context = {'cat':cat}
    return Response(context,status=HTTP_200_OK)

def allcourse(request):
    course = Maincourseserial(MainCourse.objects.all(), many=True)
    context = {'course':course}
    return Response(context,status=HTTP_200_OK)

def edit_post(request, id):
    if request.method == 'POST':
        posts = Post.objects.get(id=id)
        editpost= Postserial(request.POST or None, request.FILES or None, instance=posts, partial=True) # Added partial = true
        if editpost.is_valid():
            editpost.save()
        messages.success(request, "Post Update Sucessfully !!")
        # return redirect('allposts')
        return Response(status=HTTP_200_OK)
        
    else:
        posts = Post.objects.get(id=id)
        editpost= EditPostserial(instance=posts)
        context = {'editpost':editpost}

    return Response(context,status=HTTP_200_OK)
    
def delete_post(request, id):
    delete = Post.objects.get(pk=id)  #pk means primary key
    delete.delete()
    messages.success(request, "Post Deleted Successfully.")
    return Response(status=HTTP_204_NO_CONTENT)


#For edit the categories
def edit_cat(request, id):
    if request.method == 'POST':
        cat = Category.objects.get(id=id)
        editcat= Catserial(request.POST or None, request.FILES or None, instance=cat,partial=True)
        if editcat.is_valid():
            editcat.save()
            messages.success(request, "Category Update Sucessfully !!")
            # return redirect('allcat')
            return Response(status=HTTP_201_CREATED)
        else:
            messages.warning(request, "Category is not Updated !!")
            return redirect('allcat')    
    else:
        cat = Category.objects.get(id=id)
        editcat= Catserial(instance=cat)
        context= {'editcat':editcat}

    return Response(context,status=HTTP_200_OK)

#For delete the categories    
def delete_cat(request, id):
    delete = Category.objects.get(pk=id)  #pk means primary key
    delete.delete()
    messages.success(request, "Category Deleted Successfully.")
    # return redirect('allcat')
    return Response(status=HTTP_204_NO_CONTENT)


#For edit the course
def edit_course(request, id):
    if request.method == 'POST':
        course = MainCourse.objects.get(id=id)
        editcourse= Maincourseserial(request.POST or None, request.FILES or None, instance=course,partial=True)
        if editcourse.is_valid():
            editcourse.save()
        messages.success(request, "Course Update Sucessfully !!")
        # return redirect('allcat')
        return Response(status=HTTP_201_CREATED)
    else:
        cat = MainCourse.objects.get(id=id)
        editcourse= Maincourseserial(instance=cat)
    context = {'editcourse':editcourse}
    return Response(context,status=HTTP_200_OK)

#For delete the course
def delete_course(request, id):
    delete = MainCourse.objects.get(pk=id)  #pk means primary key
    delete.delete()
    messages.success(request, "MainCourse Deleted Successfully.")
    # return redirect('allcourses')
    return Response(status=HTTP_204_NO_CONTENT)

def add_videos(request):
    video= videoserial()
    if request.method=='POST':
        video=videoserial(request.POST, request.FILES)
        if video.is_valid():
            video.save()
        messages.success(request, "video Added Sucessfully !!")    
        # return redirect('home')
        return Response(status=HTTP_201_CREATED)
    context = {'video':video}
    return Response(context,status=HTTP_200_OK)

def edit_videos(request, id):
    if request.method == 'POST':
        vid = video.objects.get(id=id)
        editvideo= videoserial(request.POST or None, request.FILES or None, instance=vid, partial=True)
        if editvideo.is_valid():
            editvideo.save()
        messages.success(request, "Video Update Sucessfully !!")
        # return redirect('allcat')
        return Response(status=HTTP_205_RESET_CONTENT)
        
    else:
        vid = video.objects.get(id=id)
        editvideo= videoserial(instance=vid)
        context = {'editvideo':editvideo}
        return Response(context,status=HTTP_200_OK)

def delete_video(request, id):
    delete = video.objects.get(pk=id)  #pk means primary key
    delete.delete()
    messages.success(request, "video Deleted Successfully.")
    # return redirect('allcourses')
    return Response(status=HTTP_204_NO_CONTENT)   

def allvideos(request):
    vid = videoserial(video.objects.all(), many=True)
    context = {'video':vid}
    return Response(context,status=HTTP_200_OK)

def paid_video(request, slug):
    vid = videoserial(video.objects.filter(post=allpost), many=True)
    context = {'allpost':allpost, 'vid':vid}
    return Response(context,status=HTTP_200_OK)
   

def alltime(request):
    f = timing.objects.all()                                                # Create a time serializers
    context = {'f':f}
    return Response(context,status=HTTP_200_OK)
    

def add_time(request):
    time= timingserial()                     #Created serializer
    if request.method=='POST':
        time= timingserial(request.POST, request.FILES)
        if time.is_valid():
            time.save()
        messages.success(request, "Timing Added Sucessfully !!")    
        # return redirect('alltime')
        return Response(status=HTTP_201_CREATED)
    context = {'time':time}
    return Response(context,status=HTTP_200_OK)

def edit_time(request, id):
    if request.method == 'POST':
        time = timing.objects.get(id=id)
        Edittiming= timingserial(request.POST, instance=time, partial=True)
        if Edittiming.is_valid():
            Edittiming.save()
        messages.success(request, "Timing Update Sucessfully !!")
        # return redirect('alltime')
        return Response(status=HTTP_205_RESET_CONTENT)
        
    else:
        time = timing.objects.get(id=id)
        Edittiming= timingserial(instance=time)   
        context = {'time':Edittiming}
        return Response(context,status=HTTP_200_OK)      

def delete_time(request, id):
    delete = timing.objects.get(pk=id)  #pk means primary key
    delete.delete()
    messages.success(request, "Timing Deleted Successfully.")
    # return redirect('alltime')
    return Response(status=HTTP_204_NO_CONTENT)

def allsubcatg(request):
    f = subcatg(subcat.objects.all(), many=True)
    context = {'f':f}
    return Response(context,status=HTTP_200_OK) 

def add_subcatg(request):
    sub= subcatg()
    if request.method=='POST':
        sub= subcatg(request.POST, request.FILES)
        if sub.is_valid():
            sub.save()
        messages.success(request, "Subcat Added Sucessfully !!") 
        return Response(status=HTTP_201_CREATED)   
        # return redirect('allsubcatg')
        context = {'sub':sub}
    return Response(context,status=HTTP_200_OK)

def edit_subcatg(request, id):
    if request.method == 'POST':
        sub = subcat.objects.get(id=id)
        editsub = subcatg(request.POST, instance=sub, partial=True)
        if editsub.is_valid():
            editsub.save()
        messages.success(request, "Subcat Update Sucessfully !!")
        # return redirect('allsubcatg')
        return Response(status=HTTP_205_RESET_CONTENT)
        
    else:
        sub = subcat.objects.get(id=id)
        editsub = subcatg(instance=sub)   
        context = {'subcat':editsub}
    return Response(context,status=HTTP_200_OK)

def delete_subcatg(request, id):
    delete = subcat.objects.get(pk=id)  #pk means primary key
    delete.delete()
    messages.success(request, "Subcat Deleted Successfully.")
    # return redirect('allsubcatg')
    return Response(status=HTTP_204_NO_CONTENT) 

def admin_reviews(request):
    review= admin_reviewserial()
    if request.method=='POST':
        review = admin_reviewserial(request.POST, request.FILES)
        if review.is_valid():
            review.save()
        messages.success(request, "Review Added Sucessfully !!")    
        # return redirect('alladmin_review')
        return Response(status=HTTP_201_CREATED)
    context =  {'review':review}
    return Response(context,status=HTTP_200_OK)

def delete_admin_review(request, id):
    delete = Reviews.objects.get(pk=id)  #pk means primary key
    delete.delete()
    messages.success(request, "Admin Review Deleted Successfully.")
    # return redirect('alladmin_review')  
    return Response(status=HTTP_204_NO_CONTENT)

def edit_admin_review(request, id):
    if request.method == 'POST':
        review = Reviews.objects.get(id=id)
        edit_admin_reviews = admin_reviewserial(request.POST, instance=review, partial=True)
        if edit_admin_reviews .is_valid():
            edit_admin_reviews .save()
        messages.success(request, "Reviews Update Sucessfully !!")
        # return redirect('alladmin_review')
        return Response(status=HTTP_205_RESET_CONTENT)
        
    else:
        faqs = Reviews.objects.get(id=id)
        edit_admin_reviews = admin_reviewserial(instance=faqs)
        context = {'edit':edit_admin_reviews }

    return Response(context, status=HTTP_200_OK)   

def alladmin_review(request):
    review = reviewserial(Reviews.objects.all(), many=True)
    context = {'review':review}
    return Response(context,status=HTTP_200_OK)  
