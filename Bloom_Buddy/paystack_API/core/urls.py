from django.urls import path
from .views import initiate_payment, verify_payment

urlpatterns = [
    path('', initiate_payment.as_view(), name='initiate-payment'),
    path('<str:ref>/', verify_payment.as_view(), name='verify-payment'),
]
