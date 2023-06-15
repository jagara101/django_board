from django.db import models

# Create your models here.
# models.py의 클래스와 db의 table과 sync를 맞춰 테이블(컬럼정보) 자동생성.

#클래스명=테이블명, 변수=컬럼명
class Test(models.Model):  
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    password=models.CharField(max_length=30)

class Author(models.Model): #Author,Post 클래스는 models.Model을 상속받는 Django 모델, 이렇게 지정해서 views.py에서 
                            #from .models import Author, Post 이런식으로 불러올 수 있다.
    name=models.CharField(max_length=20) #name,email,password 이건 db에서 컬럼에 해당한다.
    email=models.CharField(max_length=50, unique=True)
    password=models.CharField(max_length=30)
    #DB설정에 default timestamp가 걸리는 것이 아닌, 장고가 현재시간을 db에 insert
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Post(models.Model):
    title=models.CharField(max_length=100)
    contents=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    # DB에는 fk를 설정한 변수명에 _id가 붙게 된다
    #on_delete=models.CASCADE,
    author=models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name='posts')
    '''
    ▲ Post 모델에서 author 필드를 정의하는 부분이다. author=models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    이 필드는 Author 모델과의 관계를 나타내는 외래 키(ForeignKey) 필드이다. 
    Author 모델은 게시물을 작성한 작성자를 나타낸다. 설정된 외래 키 필드는 Author 객체가 삭제되면 해당 Post 객체의
    author 필드를 NULL로 설정하고, Post 객체의 author 필드는 NULL 값을 허용한다. 이를 통해 게시물과 작성자 간의 
    관계를 형성하고 작성자를 지정할 수 있다.
    '''
    '''
    related_name='posts'는 역참조이다. 즉 author에서 post left join을 거는거나 마찬가지
    '''