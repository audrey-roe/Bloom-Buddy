
# Create your views here.
from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from django.http import JsonResponse
from .serializers import createuserserial, testformserial
from .models import *
from django.http import HttpResponse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from knox.auth import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes



from rest_framework.views import APIView

 
# Create your views here.

@api_view(['POST'])
@authentication_classes([TokenAuthentication,SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])

class mchatclass(APIView):
    # authentication_classes = [TokenAuthentication,SessionAuthentication,BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    
    def get(self, request, format = None):
        user_i = info.objects.get(user = request.user)
        print(f'info: {user_i.user_image}')
        serializer = createuserserial(user_i)
        ddata = dict(serializer.data)
        ddata['child_name'] = request.user.first_name
        ddata['child_age'] = request.user.last_name
        ddata['relation_to_child'] = request.user.caregiver_name
        ddata['caregiver_email'] = request.user.caregiver_email
        ddata['caregiver_phone'] = request.user.caregiver_phone
        ddata['relation_to_child'] = request.user.caregiver_name
        resp = {
            "data": ddata
        }
        return Response (resp)

def mchat(request):
        if request.method == 'POST':
            print(request.POST)
            questions=test.objects.all()
            score = 0
            # wrong=0
            # correct=0
            total=0
            for q in questions:
                total+=1
                print(request.POST.get(q.question))
                print(q.ans)
                print()
                if q.ans ==  request.POST.get(q.question):
                    score+=1
                #     correct+=1
                # else:
                #     wrong+=1
            context = {
                'total':total,
                'score': score
            }
            return JsonResponse(request,
            # 'test/result.html',
            context)
        else:
            questions=test.objects.all()
            context = {
                'questions':questions
            }
            
        return JsonResponse(request,
            # 'test/home.html', 
            context)