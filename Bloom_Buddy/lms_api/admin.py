from django.contrib import admin
from .models import *
# Register your models here.

class videoAdmin(admin.StackedInline):
    model = video

class timeAdmin(admin.StackedInline):
    model = timing

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'ordered']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [timeAdmin, videoAdmin]
 
    class Meta:
       model = Post

admin.site.register(Customer)
admin.site.register(MainCourse)
admin.site.register(Reviews)
admin.site.register(Category)
admin.site.register(subcat)
admin.site.register(Order, OrderAdmin)
admin.site.register(Cart)
# admin.site.register(Post)
# admin.site.register(video, videoAdmin)
admin.site.register(Comment)
# admin.site.register(timing, timeAdmin)
