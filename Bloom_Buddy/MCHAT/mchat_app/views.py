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
from django.core.paginator import Paginator , EmptyPage, PageNotAnInteger


from rest_framework.views import APIView

 
# Create your views here.



 #still editing this is not the final  
def getPAGE(request, page):
    
    questions = Question.objects.all()
    paginator = Paginator(question, per_page = 4)
    page_object = paginator.get_page(page)
    context = {"page_obj": page_object}
    return render(request, "whateverurl.html", context)
    # serializer = QuestionSerializer(questions, many=True)
    # return Response(serializer.data)


def post(self, request, format=None):
    question = Question.objects.filter(yes= 'yes')
    counter = request.POST.filter(yes='yes').count()
    
    # Count = Question.objects.filter(yes= 'yes').count()
    total_score = 23
    points = total_score - counter
    context = { 'score': points}
    # Serializer = QuestionSerializer(request.data, many=True)
    
    # serializer = QuestionSerializer(question, many=True)
    # return Response({"data": Count , "ser": serializer.data,  "serialized": Serializer.data, "your score":points}, status=status.HTTP_201_CREATED)
    return render(
        request,
        'mchat-results-page.html',
        context
        )
    
        
        
            
            
    
    
    
    
    
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    