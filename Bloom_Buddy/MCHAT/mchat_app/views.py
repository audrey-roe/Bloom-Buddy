from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from django.http import JsonResponse
from .serializers import createuserserial
from .models import *
from rest_framework import status
from django.http import Http404
from django.http import HttpResponse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializers import QuestionSerializer


from rest_framework.views import APIView

 
# Create your views here.


class mchatclass(APIView):
     
    def get(self, request, format = None):
        
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        question = Question.objects.filter(yes= 'yes')
        Count = Question.objects.filter(yes= 'yes').count()
        total_score = 23
        points = total_score - Count
        
       
        serializer = QuestionSerializer(question, many=True)
        return Response({"data": Count , "ser": serializer.data, "your score":points}, status=status.HTTP_201_CREATED)
        
            
            
        
        
       
        
        
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       