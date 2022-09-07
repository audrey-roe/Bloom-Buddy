
# Create your views here.
from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from django.http import JsonResponse
from .serializers import createuserserial, testformserial
from .models import *
from django.http import HttpResponse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes



from rest_framework.views import APIView

 
# Create your views here.

class mchatclass(APIView):

    
    def post(self, request, format = None):
        serializer = createuserserial(info.objects.get(user = request.user))
        resp = {
            "data": serializer.data
        }
        return Response (resp)


class mchat(APIView):
    def post(self, request):
        questions=test.objects.all()
        score = 0
        total=0
        for q in questions:
            total+=1
            if q.ans ==  request.data(q.question):
                score+=1
        context = {
            'total':total,
            'score': score
        }
        return Response(context)
    
    def get(self, request):
        questions= testformserial(test.objects.all(), many = True)
        
        context = {
            'questions':questions.data
        }
        
        return Response(context)