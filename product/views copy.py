from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from .models import Product

# Create your views here.

# Todo
# templates 폴더 만들고 index.html
# main 함수 만들어서 상품 리스트 나오게 하기
# 상품 리스트에는 한 줄로 상품명, 가격, 장소 나오게 하기

def main(request):
    
    products = Product.objects.all().order_by('-id')
    return render(request, 'product.html', {
        'products': products
    })

def detail(request, pk):
    product = Product.objects.get(pk=pk)
    
    if product.image:
        image = product.image.url
    else:
        image = '/static/bg.jpg'
    
    return JsonResponse({
        'title': product.title,
        'content': product.content,
        'price': product.price,
        'location': product.location,
        'image': image
    })
    
def write_template(request):
    
    if not request.session.get('user_id'):
        return redirect('/member/login/')
    
    if request.method == 'POST':
        print('자료형 체크1 ', request.method) # POST
        print('자료형 체크2 ', request.FILES.get('image')) # monitor.jpg
        
        product = Product(
            title = request.POST.get('title'),
            content = request.POST.get('content'),
            price = request.POST.get('price'),
            location = request.POST.get('location'),
            image = request.FILES.get('image')
        )
        # print(product.id) 에러 발생
        product.save()
        return redirect('/')
    
    return render(request, 'product_write2.html')
