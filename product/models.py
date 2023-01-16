from django.db import models

# Create your models here.

class Product(models.Model):
    # title, content, price, location
    
    # PK를 직접 선언하는 방법
    # id = models.IntegerField(primary_Key=True)
    
    title = models.CharField(max_length=256, verbose_name="상품 이름")
    content = models.TextField(verbose_name="상품 설명")
    price = models.IntegerField(verbose_name='상품 가격')
    location = models.CharField(max_length=500, verbose_name="상품 거래 희망 위치")   
    
    def __str__(self):
        return f"title: {self.title}, content: {self.content}, price: {self.price}, location: {self.location}" 
    
    class Meta:
        db_table = 'shinhan_product'
        verbose_name = '상품'
        verbose_name_plural = '상품(들)'        
