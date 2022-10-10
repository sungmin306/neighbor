from django.db import models

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=50, unique=True) # 닉네임 
    email = models.CharField(max_length=100, unique=True) # email
    password = models.CharField(max_length=50) # 비밀번호
    check_password = models.CharField(null=True, max_length=50) # 비밀번호 확인 용
    home = models.CharField(max_length=100) #집 주소 
    home_num = models.IntegerField() # 우편번호 
    bank = models.CharField(max_length=50) # 은행이름
    bank_num = models.CharField(max_length=50) # 계좌번호
    created_at = models.DateTimeField(auto_now_add=True) # 생성시간
    updated_at = models.DateTimeField(auto_now=True) # 업데이트 시간
    
    class Meta:
        db_table  = 'accounts'
    
class Post(models.Model): #배달하는 글 생성
    title = models.CharField(max_length=50, verbose_name="제목") # 제목
    shopName=models.CharField(null=True, max_length=50) # 가게이름
    content=models.CharField(null=True, max_length=50) # 내용
    peoNum=models.TextField(null=True) # 모집 인원
    useTime=models.CharField(null=True,max_length=50) #소요시간
    place=models.CharField(null=True,max_length=50) # 분배장소
    category=models.CharField(null=True, max_length=50) # 카테고리(선택하는것 id 값 받을 예정)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class comment(models.Model): # 댓글작성
    content= models.TextField()

#class TOgeshop