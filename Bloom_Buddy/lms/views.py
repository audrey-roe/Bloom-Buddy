from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, redirect, render
from .serializers import *
from django.contrib import messages
from django.contrib.auth import authenticate, login as loginUser, update_session_auth_hash
from django.http import HttpResponse
from time import time
from django.views.decorators.csrf import csrf_exempt
# from Bloom_Buddy.settings import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

# from knox.auth import TokenAuthentication

# import paystack #test with sandbox
# client = paystack.Client(auth=('KEY_ID', 'KEY_SECRET'))

# @api_view(['POST'])
# @authentication_classes([TokenAuthentication,SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
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
        return Response(context)


class totalposts(APIView):
    def get(self, request):
        total = Postserial(Post.objects.all(), many = True)
        context = {'total':total}
        return Response(context)

class post_by_category(APIView):
    def get(self, request, catslug):
        posts = Postserial(Post.objects.all(), many = True)
        cat_post = Postserial(Post.objects.filter(category__slug=catslug), many = True)
        allposts = Postserial(Post.objects.filter(maincourse=True), many=True)
        # slider_post = Postserial(Post.objects.filter(slider_post=True), many = True)
        top_three_catg = Catserial(Category.objects.filter(top_three_cat=True)[:3], many=True)
        main_course = Maincourseserial(MainCourse.objects.all(), many = True)
        allcat = Catserial(Category.objects.all(), many = True)
        categories = Catserial(Category.objects.filter(parent=None).order_by('-created_at')[:7], many =  True)
        # footcategories = Catserial(Category.objects.filter(parent=None)[:2], many= True)
        catg = Catserial(Category.objects.exclude(parent=None).order_by('-created_at')[:7], many = True)
        catg_parent = Catserial(Category.objects.exclude(parent=True), many=True)
        latest_catg = Catserial(Category.objects.filter(parent=None)[:5], many=True)
        latest_post = Postserial(Post.objects.order_by('-date')[:4], many = True)
        latest_catg_all = Catserial(Category.objects.filter(parent=None)[5:], many= True)
        rev = reviewserial(Reviews.objects.order_by('-created')[:6], many = True)
        context = {
                    'latest_catg_all':latest_catg_all, 
                    'rev':rev, 'posts':posts, 
                    'cat_post':cat_post,
                    'allposts':allposts, 
                    'main_course':main_course, 
                    'top_three_catg':top_three_catg, 
                    'catg':catg, 'slider_post':slider_post, 
                    'latest_catg':latest_catg, 
                    'latest_post':latest_post
                    }
        return Response(context)

class allpost_by_category(APIView):
    def get (self, request, postslug):
        posts = Postserial(Post.objects.all(), many = True)
        cat_post = Postserial(Post.objects.filter(category__slug=postslug), many = True)
        subcat_post = subcatgserial(Post.objects.filter(subcategory__slug=postslug), many= True)
        allposts = Postserial(Post.objects.filter(maincourse=True), many = True)
        allcat = Postserial(Category.objects.all(), many = True)
        context = {
                    'posts':posts,
                    'subcat_post':subcat_post, 
                    'cat_post':cat_post,
                    'allposts':allposts,
                    'allcat':allcat,
                    }  
        return Response(context)

class subcat_by_category(APIView):
    def get (self, request, subcatslug):
        # allcats = get_object_or_404(Category, slug=subcatslug)
        category = subcatgserial(subcat.objects.filter(slug=subcatslug), many= True)
        # allsubcatg = allcats.subcat.filter(parent__slug=slug)
        cat_subcat = subcatgserial(subcat.objects.filter(parent__slug=subcatslug), many= True)
        context = {
                    'cat_subcat':cat_subcat, 
                    'category':category, 
                    'allcats':allcats
                    }
        return Response(context)
    
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

        context = {
                    'posts':posts, 
                    'category':category, 
                    'allcat':allcat, 
                    'catg_parent':catg_parent, 
                    'allpost':allpost, 
                    'reviews':reviews, 
                    'time':time, 
                    'videos':vid
                    }
        return Response (context)
    
    def post(self, request, data):
        Reviews.objects.create(
            post=Post.objects.get(
                id = request.data['rev_id']),
                user=request.user,
                stars=request.data['no_o_stars'],
                content=request.data['content']
            )
        return Response({
            'message' : 'successfully added review'
        })

class search(APIView):

    def get(self, request):
        search = request.GET['search']
        totalposts = Postserial(Post.objects.filter(title__icontains=search), many = True)
        context = {
                    'totalposts':totalposts, 
                    'search':search
                    }
        return Response(context)

class video(APIView):
    def get(self, request):
        return Response(status=HTTP_200_OK)

    def addVideosWatched(self, request, video_id):
        pass

class course(APIView):

    def get(self, request):
        main_course = Maincourseserialserial(MainCourse.objects.all(), many = True)
        context = {'main_course':main_course}
        return Response(context)

# @csrf_exempt
@api_view(['POST'])
def verify_payment(self, request):
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
                return Response({
            'message' : "Invalid Payment Details"
        })
        # def get(self, request):
        #         cart_items = Cart.objects.filter(user=request.user, purchase=False)
        #         for item in cart_items:
        #             item.purchase = True
        #             item.save()
        #         return redirect('home')    

        # def post(self, request):
        #     client.utility.verify_payment_signature(data)
        #     paystack_order_id = data['paystack_order_id']
        #     paystack_payment_id = data['paystack_payment_id']
        #     order = Order.objects.get(order_id = paystack_order_id)
        #     order.payment_id = paystack_payment_id
        #     order.ordered = True
        #     order.save() # i remembered the save this time

        #     return Response({
        #     'message' : "Invalid Payment Details"
        # })

class logout(APIView):
    def post(self, request):
        request.session.clear()
       # return redirect('home') 
        return Response(status=HTTP_200_OK)

class logout(APIView):
    def userdashboard(self, request):
        customer = Customerserial(Customer.objects.all(), many=True)
        carts = CartSerial(Cart.objects.filter(user=request.user, purchase=True, many =True))
        orders = OrderSerializer(Order.objects.filter(user=request.user, ordered=True), many =True)
        context = {
                    'carts':carts,
                    'customer':customer, 
                    'orders':orders
                }

        return Response(context)

class userprofile(APIView):
    def get(self, request):
        customer = CustomerAuthserial(Customer.objects.get(user_id=request.user.id), many = True)
        context = {'customer':customer}
        return Response(context)

class remove_from_cart(APIView):
    def post(self, request, id):
        item = get_object_or_404(Post, id=id)
        order_obj = Order.objects.filter(user=request.user, ordered=False)
        if order_obj.exists():
            order = order_obj[0]
            if order.orderitems.filter(item=item).exists():
                order_item = Cart.objects.filter(item=item, user=request.user, purchase=False)[0]
                order.orderitems.remove(order_item)
                order_item.delete()
                return  Response({'message': "This product is removed from your cart"})
            else:
                return Response({
                'message' : "This item was not in your cart"
            })
        else:
            return Response({
                'message' : "You don't have an active order"
            })



class checkout(APIView):
    def get(self, request):
        user = None
        # coupon = promocode.objects.all()
        # if request.method == 'get':
        try:
            orders = Order.objects.get(user=request.user, ordered=False)
            context = {'orders':orders}
            return Response(context)
        except ObjectDoesNotExist:
            return Response({'message': "You don't have an active order"})
    
    def post(self, request, data):
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
        return Response(context)


def webadmin(request):
    postcount = Post.objects.count()
    catcount = Category.objects.count()
    usercount = User.objects.count()
    orders = Order.objects.all()
    context = {'postcount':postcount, 'cat':catcount, 'user':usercount,"orders":orders}
    return render(request, 'index.html', context)  

def add_post(request):
    posts= Postserial()
    if request.method=='POST':
        posts=Postserial(request.POST, request.FILES)
        if posts.is_valid():
            posts.save()
        messages.success(request, "Posts Added Sucessfully !!")    
        return redirect('allposts')
    return render(request, "admin/addpost.html", {'post':posts})


def add_course(request):
    course= Maincourseserial()
    if request.method=='POST':
        course=Maincourseserial(request.POST, request.FILES)
        if course.is_valid():
            course.save()
        messages.success(request, "Course Added Sucessfully !!")    
        return redirect('allcourses')
    return render(request, "admin/addcourse.html", {'course':course})


def add_cat(request):
    category= Catserial()
    if request.method=='POST':
        category=Catserial(request.POST, request.FILES)
        if category.is_valid():
            category.save()
        messages.success(request, "category Added Sucessfully !!")    
        return redirect('allcat')
    return render(request, "admin/addcat.html", {'category':category})

def add_curriculam(request):
    category= Catserial()
    if request.method=='POST':
        category=Catserial(request.POST, request.FILES)
        if category.is_valid():
            category.save()
        messages.success(request, "category Added Sucessfully !!")    
        return redirect('admin')
    return render(request, "admin/addcat.html", {'category':category})

#This is for show all Posts in Custom Admin Panel
def allposts(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'admin/allposts.html', context)

#This is for show all Users in Custom Admin Panel
def allusers(request):
    # users = User.objects.all()
    customer = Customer.objects.all()
    context = {
        # 'users':users
    'customer':customer
    }
    return render(request, 'admin/allusers.html', context)

def userdetails(request, id):
    customer = Customer.objects.filter(id=id).first()
    context = {'customer':customer}
    return render(request, 'admin/user_detail.html', context)

def allorders(request):
    orders = Order.objects.filter(ordered=True)
    carts = Cart.objects.all()
    context = {
    'orders':orders, 'carts':carts,
    }
    return render(request, 'admin/allorders.html', context)


#This is for show all Categories in Custom Admin Panel
def allcat(request):
    cat = Category.objects.filter(parent=None).order_by('hit')
    context = {'cat':cat}
    return render(request, 'admin/allcat.html', context)

def allcourse(request):
    course = MainCourse.objects.all()
    context = {'course':course}
    return render(request, 'admin/allcourse.html', context)

def edit_post(request, id):
    if request.method == 'POST':
        posts = Post.objects.get(id=id)
        editpost= EditPostserial(request.POST or None, request.FILES or None, instance=posts)
        if editpost.is_valid():
            editpost.save()
        messages.success(request, "Post Update Sucessfully !!")
        return redirect('allposts')
    else:
        posts = Post.objects.get(id=id)
        editpost= EditPostserial(instance=posts)

    return render(request, "admin/editposts.html", {'editpost':editpost})
    
def delete_post(request, id):
    delete = Post.objects.get(pk=id)  #pk means primary key
    delete.delete()
    messages.success(request, "Post Deleted Successfully.")
    return redirect('allposts')


#For edit the categories
def edit_cat(request, id):
    if request.method == 'POST':
        cat = Category.objects.get(id=id)
        editcat= Catserial(request.POST or None, request.FILES or None, instance=cat)
        if editcat.is_valid():
            editcat.save()
            messages.success(request, "Category Update Sucessfully !!")
            return redirect('allcat')
        else:
            messages.warning(request, "Category is not Updated !!")
            return redirect('allcat')    
    else:
        cat = Category.objects.get(id=id)
        editcat= Catserial(instance=cat)

    return render(request, "admin/editcat.html", {'editcat':editcat})

#For delete the categories    
def delete_cat(request, id):
    delete = Category.objects.get(pk=id)  #pk means primary key
    delete.delete()
    messages.success(request, "Category Deleted Successfully.")
    return redirect('allcat')


#For edit the course
def edit_course(request, id):
    if request.method == 'POST':
        course = MainCourse.objects.get(id=id)
        editcourse= EditMaincourseserial(request.POST or None, request.FILES or None, instance=course)
        if editcourse.is_valid():
            editcourse.save()
        messages.success(request, "Course Update Sucessfully !!")
        return redirect('allcat')
    else:
        cat = MainCourse.objects.get(id=id)
        editcourse= EditMaincourseserial(instance=cat)

    return render(request, "admin/editcourse.html", {'editcourse':editcourse})

#For delete the course
def delete_course(request, id):
    delete = MainCourse.objects.get(pk=id)  #pk means primary key
    delete.delete()
    messages.success(request, "MainCourse Deleted Successfully.")
    return redirect('allcourses')

def add_videos(request):
    video= videoserial()
    if request.method=='POST':
        video=videoserial(request.POST, request.FILES)
        if video.is_valid():
            video.save()
        messages.success(request, "video Added Sucessfully !!")    
        return redirect('home')
    return render(request, "admin/addvideo.html", {'video':video})

def edit_videos(request, id):
    if request.method == 'POST':
        vid = video.objects.get(id=id)
        editvideo= videoserial(request.POST or None, request.FILES or None, instance=vid)
        if editvideo.is_valid():
            editvideo.save()
        messages.success(request, "Video Update Sucessfully !!")
        return redirect('allcat')
    else:
        vid = video.objects.get(id=id)
        editvideo= videoserial(instance=vid)

    return render(request, "admin/editvideo.html", {'editvideo':editvideo})

def delete_video(request, id):
    delete = video.objects.get(pk=id)  #pk means primary key
    delete.delete()
    messages.success(request, "video Deleted Successfully.")
    return redirect('allcourses')   

def allvideos(request):
    vid = video.objects.all()
    context = {'video':vid}
    return render(request, 'admin/allvideo.html', context)

def paid_video(request, slug):
    allpost = get_object_or_404(Post, slug=slug)
    vid = video.objects.filter(post=allpost)
    context = {'allpost':allpost, 'vid':vid}
    return render(request, 'paidvideo.html', context)

def alltime(request):
    f = timing.objects.all()
    context = {'f':f}
    return render(request, 'admin/alltime.html', context)

def add_time(request):
    time= timingserial()
    if request.method=='POST':
        time= timingserial(request.POST, request.FILES)
        if time.is_valid():
            time.save()
        messages.success(request, "Timing Added Sucessfully !!")    
        return redirect('alltime')
    return render(request, "admin/add_time.html", {'time':time})

def edit_time(request, id):
    if request.method == 'POST':
        time = timing.objects.get(id=id)
        Edittiming= timingserial(request.POST, instance=time)
        if Edittiming.is_valid():
            Edittiming.save()
        messages.success(request, "Timing Update Sucessfully !!")
        return redirect('alltime')
    else:
        time = timing.objects.get(id=id)
        Edittiming= timingserial(instance=time)   

    return render(request, "admin/edit_time.html", {'time':Edittiming})

def delete_time(request, id):
    delete = timing.objects.get(pk=id)  #pk means primary key
    delete.delete()
    messages.success(request, "Timing Deleted Successfully.")
    return redirect('alltime') 

def allsubcatg(request):
    f = subcat.objects.all()
    context = {'f':f}
    return render(request, 'admin/allsubcat.html', context)

def add_subcatg(request):
    sub= subcatg()
    if request.method=='POST':
        sub= subcatg(request.POST, request.FILES)
        if sub.is_valid():
            sub.save()
        messages.success(request, "Subcat Added Sucessfully !!")    
        return redirect('allsubcatg')
    return render(request, "admin/add_subcat.html", {'sub':sub})

def edit_subcatg(request, id):
    if request.method == 'POST':
        sub = subcat.objects.get(id=id)
        editsub = subcatg(request.POST, instance=sub)
        if editsub.is_valid():
            editsub.save()
        messages.success(request, "Subcat Update Sucessfully !!")
        return redirect('allsubcatg')
    else:
        sub = subcat.objects.get(id=id)
        editsub = subcatg(instance=sub)   

    return render(request, "admin/edit_subcat.html", {'subcat':editsub })

def delete_subcatg(request, id):
    delete = subcat.objects.get(pk=id)  #pk means primary key
    delete.delete()
    messages.success(request, "Subcat Deleted Successfully.")
    return redirect('allsubcatg') 

def admin_reviews(request):
    review= admin_reviewserial()
    if request.method=='POST':
        review = admin_reviewserial(request.POST, request.FILES)
        if review.is_valid():
            review.save()
        messages.success(request, "Review Added Sucessfully !!")    
        return redirect('alladmin_review')
    return render(request, "admin/add_reviews.html", {'review':review})

def delete_admin_review(request, id):
    delete = Reviews.objects.get(pk=id)  #pk means primary key
    delete.delete()
    messages.success(request, "Admin Review Deleted Successfully.")
    return redirect('alladmin_review')   

def edit_admin_review(request, id):
    if request.method == 'POST':
        review = Reviews.objects.get(id=id)
        edit_admin_reviews = admin_reviewserial(request.POST, instance=review)
        if edit_admin_reviews .is_valid():
            edit_admin_reviews .save()
        messages.success(request, "Reviews Update Sucessfully !!")
        return redirect('alladmin_review')
    else:
        faqs = Reviews.objects.get(id=id)
        edit_admin_reviews = admin_reviewserial(instance=faqs)

    return render(request, "admin/edit_admin_reviews.html", {'edit':edit_admin_reviews })    

def alladmin_review(request):
    review = Reviews.objects.all()
    context = {'review':review}
    return render(request, 'admin/all_reviews.html', context)    
