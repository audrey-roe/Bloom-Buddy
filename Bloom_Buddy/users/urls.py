from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.sign_up, name='sign_up'),
    path('user_subscribe', views.user_subscribe, name='user_subscribe'),
    path('<pk>/subscription', views.user_subscribe, name='user_subscribe'),
]
