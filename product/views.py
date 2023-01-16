from django.shortcuts import render
from .models import Product

# Create your views here.

# Todo
# templates 폴더 만들고 index.html
# main 함수 만들어서 상품 리스트 나오게 하기
# 상품 리스트에는 한 줄로 상품명, 가격, 장소 나오게 하기

def main(request):
    
    products = Product.objects.all()    
    return render(request, 'product.html', {
        'products': products
    })
