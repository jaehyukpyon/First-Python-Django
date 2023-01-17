from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    # title, content, price, location
    
    # PK를 직접 선언하는 방법
    # id = models.IntegerField(primary_Key=True)
    
    # models.SET_NULL if default=1
    # models.SET_DEFAULT if null=True
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="회원")
    
    title = models.CharField(max_length=256, verbose_name="상품 이름")
    content = models.TextField(verbose_name="상품 설명")
    price = models.IntegerField(verbose_name='상품 가격')
    location = models.CharField(max_length=500, verbose_name="상품 거래 희망 위치")  
    image = models.FileField(null=True, blank=True, verbose_name="상품 이미지") # null true는 데이터베이스의 자료형, blank=true는 파이썬 코드 안에서 값을 안 넣어도 된다.
    
    def __str__(self):
        return f"title: {self.title}, content: {self.content}, price: {self.price}, location: {self.location}" 
    
    class Meta:
        db_table = 'shinhan_product'
        verbose_name = '상품'
        verbose_name_plural = '상품(들)'        
