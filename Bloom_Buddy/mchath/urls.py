from . import views
from django.urls import path

# class MyRegistrationView(RegistrationView):
#     def get_success_url(self,request, user):
#         return '/home/'

urlpatterns = [
    path('mchat/', views.mchat()),
]