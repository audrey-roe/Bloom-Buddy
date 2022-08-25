from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import  Group
from .models import *


   
   
@login_required(login_url="/login")
# @permission_required("main.add_ member", login_url="/login", raise_exception=True)
def user_subscribe(request):
    if request.method == 'POST':
        form = UpdateUserForm(request.POST)
        if form.is_valid():
           member = form.save(commit=False)
           member.name = request.user
           member.save()
           return redirect("/subscription")
    else:
        form =UpdateUserForm()

    return render(request, 'main/user_subscribe.html', {"form": form})


@login_required(login_url="/login")
def Profile(request,user_name):
    inst =get_object(Post, user_name=pk)
    user_form = UpdateUserForm(instance=inst)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=inst)
        if user_form.is_valid():
            user_form.save()
            return redirect(to='<pk>/subscription')
            context= {'user_form': user_form}
            return render(request, 'users_update.html', context)
           
    





def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/user_subscribe')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})
