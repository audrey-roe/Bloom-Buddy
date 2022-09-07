from . import views
from django.urls import path

# class MyRegistrationView(RegistrationView):
#     def get_success_url(self,request, user):
#         return '/mchat/'

urlpatterns = [
    path('mchat/', views.mchat, name='mchat'),
    path('quizz/', views.quizz, name='quizz'),
    path('instruction/', views.instruction, name='instruction'),
    path('registerPage/', views.registerPage, name='registerPage'),
    # path('registerPage_post/', views.registerPage_post, name='registerPage_post'),
]