from django.shortcuts import render, redirect
from .models import Author, Post

def home(request):
    return render(request, 'home.html')

def author_list(request):
    authors=Author.objects.all()
    return render(request, 'author/author_list.html', {'authors':authors})

def author_detail(request, my_id):
    author=Author.objects.get(id=my_id)
    return render(request, 'author/author_detail.html', {'author':author})

def author_update(request, my_id):
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

def post_list(request):
    return render(request, 'post/post_list.html')

def author_new(request):
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
    

