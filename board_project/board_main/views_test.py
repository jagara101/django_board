from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
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
        name = request.POST['my_name']
        email = request.POST['my_email']
        password = request.POST['my_password']
        print(name,email,password)
        return redirect('/') #localhost:8000로 간거랑 똑같음
    else:
        return render(request, 'test/test_post_form.html')
