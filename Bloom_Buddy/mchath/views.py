# Create your views here.
from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from .forms import createuserform, quizform
from .models import quiz, customer
from django.http import HttpResponse

# Create your views here.
def registerPage(request):
    return render(request, 'signinfo.html')

# def registerPage_post(request):
#     return redirect('quizz')        
#     else:  
#         form = createuserform()
#         if request.method=='POST':
#             form = createuserform(request.POST)
#             if form.is_valid() :
#                 user=form.save()
#                 return redirect('login')
#         context={
#             'form':form,
#         }
#         return render(request, 'quiz.html', context)
            

def registerPage_post(request):            
        if request.method=='POST':
            customer.objects.create(
                caregiver_name = request.POST['caregiver_name', ],
                child_age = request.POST['child_age'],
                child_name = request.POST['child_name'],
                caregiver_email = request.POST['caregiver_email'],
                caregiver_phone = int(f"234{(request.POST['phone'].replace('+','')).replace('234234','').replace('234','')}"),
                date = request.POST['date'],)

        return render(request, 'quiz.html')    

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
            'mchat-results-page.html',
            context
            )
    else:
        questions=quiz.objects.all()
        context = {
            'questions':questions
        }
    
    return render(request, 'quiz.html', context)

