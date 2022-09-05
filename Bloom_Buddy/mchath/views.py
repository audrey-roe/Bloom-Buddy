# Create your views here.
from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from .forms import *
from .models import *
from django.http import HttpResponse

# Create your views here.

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
        return render(request,
        # 'test/result.html',
        context)
    else:
        questions=test.objects.all()
        context = {
            'questions':questions
        }

    return render(request,
        # 'test/home.html', 
        context)