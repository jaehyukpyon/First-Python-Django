from django.shortcuts import render, redirect
from django.http.response import HttpResponse
#from .models import Member
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
 
# Create your views here.

def main(request):
    pass

def signin(request):
    
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')
        user = authenticate(request, username=user_id, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
            
    # 로그인 실패
    return render(request, 'login.html')

def signout(request):    
    
    return redirect('/')

def register(request):
    if request.method == 'POST':
        User.objects.create_user(
            request.POST.get('user_id'),
            request.POST.get('email'),
            request.POST.get('password')            
        )    
        return redirect('/member/login/')
    return render(request, 'register.html')
