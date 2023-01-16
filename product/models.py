from django.db import models

# Create your models here.

class Product(models.Model):
    # title, content, price, location
    
    title = models.CharField(max_length=256, verbose_name="상품 이름")
    content = models.TextField(verbose_name="상품 설명")
    price = models.IntegerField(verbose_name='상품 가격')
    location = models.CharField(max_length=500, verbose_name="상품 거래 희망 위치")    
    
    class Meta:
        db_table = 'shinhan_product'
        
