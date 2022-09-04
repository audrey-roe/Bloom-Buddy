from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class Customer(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    # profile_pic= models.ImageField(upload_to='media/profile_pic',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name

class MainCourse(models.Model):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title', unique=True, null=False, editable=True)
    disc = models.BooleanField(default=False, verbose_name='Add In Disclaimer')

    def __str__(self):
        return self.title

class Category(models.Model):
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank = True, null=True)
    title = models.CharField(max_length=100) 
    slug = AutoSlugField(populate_from='title', unique=True, null=False, editable=True)
    logo = models.ImageField(upload_to='media/placeholder', blank=True, null=True, help_text='Optional')
    top_three_cat = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    disc = models.BooleanField(default=False, verbose_name='Add In Disclaimer')

    def __str__(self):
        return self.title

    def post_count(self):
        return self.posts.all().count()    

    class Meta:
        unique_together = ('slug', 'parent',)    
        verbose_name_plural = "categories"     

    def __str__(self):                           
        full_path = [self.title]                  
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' -> '.join(full_path[::-1])  

class subcat(models.Model):
    parent = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcat', blank = True, null=True, help_text='Select Only Sub Category')
    title = models.CharField(max_length=100) 
    slug = AutoSlugField(populate_from='title', unique=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    disc = models.BooleanField(default=False, verbose_name='Add In Disclaimer')

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('slug', 'parent')
        #This is for outside or main which shows outside panel.    
        verbose_name_plural = "Sub Categories"     

    def __str__(self):                           
        full_path = [self.title]                  
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' -> '.join(full_path[::-1])

class Post(models.Model):
    title = models.CharField(max_length=500)
    # meta_tags = models.CharField(max_length=2000, blank=True)
    # meta_desc = models.TextField(max_length=2000, blank=True)
    slug = AutoSlugField(populate_from='title', max_length=500, unique=True, null=False)
    # logo = models.ImageField(upload_to='media/placeholder') #If user want to add logo(Slider and Post) 
    desc = models.CharField(max_length=2000, blank=True, null=True)
    #for live classes or offline classes
    # badge = models.CharField(max_length=70)
    youtube = models.URLField(max_length=500, default='' )
    author = models.CharField(max_length=20, default="admin" )
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1, related_name="posts")
    subcategory = models.ForeignKey(subcat, on_delete=models.CASCADE, default=1, related_name="subcat", blank=True, null=True)
    hit = models.PositiveIntegerField(default=0) #This field is for popular posts
    maincourse = models.ManyToManyField(MainCourse, blank=True, related_name='posts')
    price = models.IntegerField(default=0)
    old_price = models.IntegerField(default=0)
    discount = models.IntegerField()
    file = models.FileField(upload_to='media/placeholder', null=True, blank=True)
    disclaimer = models.BooleanField(default=False, verbose_name='Add In Disclaimer')
    
    def __str__(self):
        return self.title    
        
    def get_rating(self):
        total = sum(float(review['stars']) for review in self.review.values() )

        return total / self.reviews.count()


class timing(models.Model):    
    date = models.CharField(max_length=100, blank=True, null=True)
    # day_duration = models.CharField(max_length=100, blank=True, null=True)
    time_duration = models.DurationField(max_length=100, blank=True, null=True)
    # time_duration2 = models.CharField(max_length=100, blank=True, null=True)
    Post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='time_posts')

class video(models.Model):
    title = models.CharField(max_length=100, null=False)
    caption = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='videos')
    vid = models.FileField(null=False)
    video_id = models.CharField(max_length=100)
    is_preview = models.BooleanField(default=False)
    desc = models.CharField(max_length= 2000, blank=True, null=True)
    duration_of_the_vid = models.DurationField(timing, blank=False, null=False)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='comments'
    )
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name) 

class Reviews(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    content = models.TextField(blank=True, null=True)
    stars = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)   

class Cart(models.Model):
    cart_id = models.CharField(max_length=500, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')
    item = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='item')
    purchase = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # certificate = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.item}'

    def get_total(self):
        total = self.item.price
        float_total = format(total, '0.2f')
        return float_total    
        
class Order(models.Model):
    # method = (
    #     ('EMI', "EMI"),
    #     ('ONLINE', "Online"),
    # )
    orderitems = models.ManyToManyField(Cart)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    phone = models.CharField(max_length=10, null = False, default='0')
    # coupon = models.ForeignKey(on_delete=models.SET_NULL, blank=True, null=True)
    total = models.DecimalField(max_digits=10, default=0, decimal_places=2, verbose_name='INR ORDER TOTAL')
    email = models.EmailField(max_length=250, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    payment_id = models.CharField(max_length=100, null=True)
    order_id =  models.CharField(max_length=100, null=True)

    def get_totals(self):
        total = 0
        for order_item in self.orderitems.all():
            total += float(order_item.get_total())
        # if self.coupon:    
        #     total -= self.coupon.amount    
        return total

# class messages():
    # pass