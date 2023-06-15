from django.shortcuts import render, redirect
'''
render 함수는 HTML 템플릿을 렌더링하여 클라이언트에게 응답을 반환 ▲
redirect 함수는 주어진 URL로 리디렉션(다른 페이지로 이동)하는 함수
'''
from . models import Author, Post  #models.py에서 만든 클래스를 불러오는 작업
from django.http import HttpResponse, HttpResponseNotFound

def home(request): #홈 화면
    return render(request, 'home.html')

def author_list(request): #회원 목록
    authors=Author.objects.all()
    return render(request, 'author/author_list.html', {'authors':authors})

def author_detail(request, my_id): #회원 상세 정보
    author=Author.objects.get(id=my_id)
    author.posts.count()
    return render(request, 'author/author_detail.html', {'author':author})

def author_update(request, my_id):  #회원 정보 수정
    author=Author.objects.get(id=my_id)
    if request.method =='POST':
        my_name = request.POST['my_name']
        my_email = request.POST['my_email']
        my_password = request.POST['my_password']
        author.name=my_name
        author.email=my_email   
        author.password=my_password
        author.save() 
        return redirect('/')
    else:
        return render(request, 'author/author_update.html', {'author':author})
    
def author_new(request): #회원 가입
    if request.method =='POST':
        my_name = request.POST['my_name']
        my_email = request.POST['my_email']
        my_password = request.POST['my_password']
        a1=Author()
        a1.name=my_name
        a1.email=my_email
        a1.password=my_password
        a1.save()      
        return redirect('/') 
    else:
        return render(request, 'author/author_new.html')
    

def post_list(request): #게시판 목록
    posts=Post.objects.filter().order_by('-created_at') #order_by하고 -컬럼명 이렇게 주면 내림차순 정렬
    return render(request, 'post/post_list.html',{'posts':posts})

def post_new(request): #게시글 쓰기
    if request.method =='POST':
        my_title = request.POST['my_title']
        my_contents = request.POST['my_contents']
        my_email = request.POST['my_email']
        p1=Post()
        
        if my_email:
            try:
                a1=Author.objects.get(email=my_email)
                #장고에서 a1객체에서 id값만 빼서, db에 저장할때는 author_id에 id값을 저장
                p1.author=a1 #{id:1, name:"hong", email:hong@naver.com...}
            except Author.DoesNotExist:
                #HttpResponse는 개발자도구 네트워크에서 200정상 출력됨
                return HttpResponseNotFound("존재하지 않는 이메일입니다.")
        p1.title=my_title
        p1.contents=my_contents
        p1.save()
        return redirect('/') 
    else:
        return render(request, 'post/post_new.html')
    
def post_detail(request, my_id): #게시글 상세정보
    post=Post.objects.get(id=my_id)
    return render(request, 'post/post_detail.html', {'post':post})


def post_update(request, my_id):  #게시글 수정
    post=Post.objects.get(id=my_id)
    if request.method =='POST':
        my_title = request.POST['my_title']
        my_contents = request.POST['my_contents']
        post.title=my_title
        post.contetns=my_contents   
        post.save() 
        return redirect('/')
    else:
        return render(request, 'post/post_update.html', {'post':post})

    

