from . import views
from django.urls import path

# class MyRegistrationView(RegistrationView):
#     def get_success_url(self,request, user):
#         return '/mchat/'

urlpatterns = [
    path('mchat/', views.mchat, name='mchat'),
    path('quiz/', views.quiz, name='quiz'),
    path('instruction/', views.instruction, name='instruction'),
    path('registerPage/', views.registerPage, name='registerPage'),
]