from django.db import models
# Create your models here.

class Member(models.Model):
    user_id = models.CharField(max_length=128, verbose_name='아이디', unique=True)
    password = models.CharField(max_length=256, verbose_name='비밀번호')
    name = models.CharField(max_length=128, verbose_name='이름')
    age = models.IntegerField(verbose_name='나이')
    
    def __str__(self):
        return f'name: {self.name}, age: {self.age}, user_id: {self.user_id}, password: {self.password}'
    
    class Meta:
        verbose_name = '회원'
        verbose_name_plural = '회원(들)'
