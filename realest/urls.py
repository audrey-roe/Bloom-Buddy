from django.urls import path
from . import views

urlpatterns = [
  path('property-types', views.realEstate_OffersViews.as_view()),
  path('real-estates', views.realEstate_property.as_view()),

]