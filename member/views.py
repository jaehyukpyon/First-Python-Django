from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Member

# Create your views here.

def main(request):
    # return HttpResponse('Hello!') # text 자체를 반환할 수 있는 HttpResponse
    # return render(request, 'index.html')
    
    # member = Member()
    # member.name = '테스트'
    # member.age = 40
    # member.save()
    
    # return render(request, 'index.html')
    
    # member = Member.objects.get(pk=100)    
    # return render(request, 'index.html', {
    #     'member': member
    # })
    
    members = Member.objects.all()
    
    return render(request, 'index.html', {
        'members': members
    })
