from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import Member
from django.contrib.auth.hashers import check_password, make_password
 
# Create your views here.

def main(request):
    # return HttpResponse('Hello!') # text 자체를 반환할 수 있는 HttpResponse
    # return render(request, 'index.html')
    
    # member = Member()
    # member.name = '테스트'f
    # member.age = 40
    # member.save()
    
    # return render(request, 'index.html')
    
    # member = Member.objects.get(pk=100) # get() 메서드는 결과값이 정확히 하나일 때 가져오는 메서드    
    # return render(request, 'index.html', {
    #     'member': member
    # })
    
    # members = Member.objects.all()    
    # return render(request, 'index.html', {
    #     'members': members
    # })
    
    # members = Member.objects.filter(age__gte=41)
    # members = Member.objects.filter(name='신한')
    
    # members = Member.objects.filter(name__contains='테스')
    
    # members = Member.objects.filter(name__contains='테스').order_by('-age') # descending
    # return render(request, 'index.html', {
    #     'members': members
    # })
    pass

def login(request):
    
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')
        # new_member = Member(
        #     user_id = user_id,
        #     password = password
        # )
        # print(new_member)
        # return redirect('/')
        if Member.objects.filter(user_id=user_id).exists():
            member = Member.objects.get(user_id=user_id)
            
            #if member.password == password:
            if check_password(password, member.password): 
                # login 성공
                request.session['user_pk'] = member.id
                request.session['user_id'] = member.user_id
                return redirect('/')
            
    # 로그인 실패
    return render(request, 'login.html')

def logout(request):
    if 'user_pk' in request.session:
        del(request.session['user_pk'])
    if 'user_id' in request.session:
        del(request.session['user_id'])
    
    return redirect('/')

def register(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')
        enc_password = make_password(password)
        name = request.POST.get('name')
        age = request.POST.get('age')
        
        new_member = Member(
            user_id = user_id,
            password = enc_password,
            name = name,
            age = age
        ) 
        new_member.save()
        print(new_member)
        return redirect('/member/login/')
            
    return render(request, 'register.html')
