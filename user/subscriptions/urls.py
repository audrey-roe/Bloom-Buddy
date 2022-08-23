from django.urls import path


from . import views

urlpatterns = [
    path("subscribe/", views.MembershipView.as_view(), name="subscription"),
    
]