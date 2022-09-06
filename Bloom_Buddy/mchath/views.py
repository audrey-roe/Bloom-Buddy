# Create your views here.
from django.http import Http404
from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from .forms import createcustomerform, quizform
from .models import quiz, customer
from django.http import HttpResponse

# Create your views here.

# def registerPage(request):
#     if request.POST:
#         form = createcustomerform(request.POST, request.FILES)
#         print = (request.FILES)
#         if form.is_valid():
#           form.save()
#         else :
#             raise Http404
#         # return redirect(quizz)
#     context = {'form': form}
#     return render(request, 'signinfo.html', context)
def registerPage(request):
    if request.method == 'POST':     
        customer.objects.create(
                caregiver_name = request.POST['caregiver_name'],
                child_age = request.POST['child_age'],
                child_name = request.POST['child_name'],
                caregiver_email = request.POST['caregiver_email'],
                caregiver_phone = int(f"234{(request.POST['phone'].replace('+','')).replace('234234','').replace('234','')}"),
                date = request.POST['date'],)

        return redirect(quizz)
    else:
        raise Http404

def mchat(request):
    return render(request, 'mchat-survey.html')

def instruction(request):
    return render(request, 'instruction.html')

def quizz(request):
    if request.POST:
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
            'mchat-results-page.html',
            context
            )
    else:
        questions=quiz.objects.all()
        context = {
            'questions':questions
        }
    
    return render(request, 'quiz.html', context)

