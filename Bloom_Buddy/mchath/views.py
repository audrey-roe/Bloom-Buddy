# Create your views here.
from django.http import Http404
from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from .forms import createuserform, quizform
from .models import quiz, customer
from django.http import HttpResponse

# Create your views here.

def registerPage(request):
    if request.POST:
        form = createuserform(request.POST, request.FILES)
        print = (request.FILES)
        if form.is_valid():
            form.save()
        return redirect(quizz)
    return render(request, 'signinfo.html', { 'form': createuserform})
              

def mchat(request):
    return render(request, 'mchat-survey.html')

def instruction(request):
    return render(request, 'instruction.html')

def quizz(request):
    if request.method == 'POST':
        print(request.POST)
        questions=quiz.objects.all()
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
            # 'total':total,
            'score': score
        }
        return render(
            request,
            'quiz.html',
            context
            )
    else:
        questions=quiz.objects.all()
        context = {
            'questions':questions
        }
    
    return render(request, 'mchat-results-page.html', context)

