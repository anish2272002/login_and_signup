from django.shortcuts import render
from time import sleep
from .models import UserProfile
from .forms import UserForm,UserProfileForm

#login imports
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.urls import reverse 
from django.contrib.auth.decorators import login_required

def index(request):
    if(request.user.is_authenticated):
        user_profile_pic=UserProfile.objects.get(user=request.user).profile_pic
        return render(request,"index.html",{'pic':user_profile_pic})
    sleep(1)
    return render(request,"index.html",{'pic':None})

'''
This save() method accepts an optional commit keyword argument, which accepts either True or False. 
If you call save() with commit=False, then it will return an object that hasn’t yet been saved to the database. 
In this case, it’s up to you to call save() on the resulting model instance. 
This is useful if you want to do custom processing on the object before saving it
'''
def signup_user(request):
    if(request.method=='POST'):
        user_form=UserForm(request.POST)
        user_profile_form=UserProfileForm(request.POST,request.FILES)
        if(user_form.is_valid() and user_profile_form.is_valid()):
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            user_profile=user_profile_form.save(commit=False)
            user_profile.user=user
            user_profile.save()
            return HttpResponseRedirect(reverse('app:login'))
        else: err=1
    else:
        err=0
        sleep(1)
        user_form=UserForm()
        user_profile_form=UserProfileForm()
    return render(request,"sign.html",{"user_form":user_form,"user_profile_form":user_profile_form,"err":err})

'''
is_active
Designates whether this user account should be considered active. We recommend that you set this flag to False 
instead of deleting accounts; that way, if your applications have any foreign keys to users, the foreign keys won’t break.
'''

def login_user(request):
    if(request.method=='POST'):
        username=request.POST['username']
        password = request.POST['password']
        user=authenticate(username=username,password=password)
        if(user):
            login(request,user)
            return HttpResponseRedirect(reverse('app:index'))
        else:
            return render(request,'acc_not_found.html',{})
    else:
        sleep(1)
    return render(request,"login.html",{})

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('app:index'))

def create(request):
    return render(request,'creator.html',{})
