from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import Member
 
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
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')
        new_member = Member(
            user_id = user_id,
            password = password
        )
        print(new_member)
        return redirect('/')
