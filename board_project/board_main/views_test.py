from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .models import Test
# Create your views here.

#get요청시 html파일 그대로 return
def test_html(request):
    return render(request, 'test/test.html')

#get요청시 html파일+data return
def test_html_data(request):
    my_name="hongildong"
    return render(request, 'test/test.html',{'name':my_name})

#get요청시 html+multi data return
def test_html_multi_data(request):
    data={'name' : 'hongildong','age': 20}
    return render(request, 'test/test.html',{'data':data})


#get요청시 data만 return
def test_json_data(request):
    data={'name' : 'hongildong','age': 20}
    #render라는 의미는 웹개발에서 일반적으로 화면을 return해줄때 사용하는 용어
    #파이썬의 dict와 유사한 json형태로 변환해서 return
    
    return JsonResponse(data)

#사용자가 get요청으로 쿼리파라미터 방식 데이터를 넣어올때
#사용자가 get요청으로 데이터를 넣어오는 방식 2가지
#1)쿼리파라미터 방식 : localhost:8000/author?id=10&name=hongildong
#2)pathvariable 방식(좀 더 현대적인 방식) : localhost:8000/author/10
def test_html_parameter_data(request):
    email=request.GET.get('email')
    name=request.GET.get('name')
    password=request.GET.get('password')
    data={'name':name, 'email':email, 'password':password}
    return render(request, 'test/test.html',{"data": data})

# http://localhost:8000/parameter_data?name=hong&email=hong@naver.com&password=1234

def test_html_parameter_data2(request, my_id):
    print(my_id)
    return render(request, 'test/test.html',{})

#form 태그를 활용한 post방식
#먼저, 화면을 rendering해주는 method



def test_post_handle(request):
    if request.method =='POST':
        my_name = request.POST['my_name']
        my_email = request.POST['my_email']
        my_password = request.POST['my_password']
       
        #db에 insert->save함수 사용
        #db에 테이블과sync가 맞는 Test라는 클래스에서 객체를 만들어 save
        '''
        t1=Test(my_name,my_email,my_password) 이런식으로도 가능하다
        '''
        t1=Test()
        t1.name=my_name
        t1.email=my_email
        t1.password=my_password
        t1.save()      
        return redirect('/') #localhost:8000로 간거랑 똑같음
    else:
        return render(request, 'test/test_post_form.html')
    
def test_select_one(request, my_id):
    #단건만 조회할때 get() 함수 사용
    t1=Test.objects.get(id=my_id)
    return render(request, 'test/test_select_one.html', {'data':t1})

def test_select_all(request):
    #모든 데이터 조회(=select*from aaa;)는 all() 함수 사용
    tests=Test.objects.all()
    # print(type(tests)) 데이터 잘 들어갔는지 확인차
    # for a in tests:
    #     print(a.name)
    return render(request, 'test/test_select_all.html',{'datas':tests})

#where조건으로 다건을 조회할땐 filter()함수 사용
#Test.object.filter(name=my_name) ->다건으로 가정
def test_select_filter(request):
    #localhost8000/test_select_filter?name=hongildong
    my_name=request.GET.get('name')
    tests=Test.objects.filter(name=my_name)
    return render(request, 'test/test_select_filter.html',{'datas':tests})

# update를 하기 위해서는 해당건을 사전에 조회하기 위한 id값이 필요
# 메서드는 등록과 동일하게 save()함수 사용
#save함수는 신규객체를 save하면 insert, 기존객체를 save하면 update
def test_update(request):
    if request.method =='POST':
        my_id = request.POST['my_id']
        t1=Test.objects.get(id=my_id)
        my_name = request.POST['my_name']
        my_email = request.POST['my_email']
        my_password = request.POST['my_password']
        print(type(my_id))
        t1.name=my_name
        t1.email=my_email   
        t1.password=my_password

        # 삭제는 delete()함수 사용. update와 마찬가지로 기존객체 조회 후 delete()
        # t1.delete()를 하면 삭제
        t1.save() 
        return redirect('/')
    else:
        return render(request, 'test/test_update.html')


     