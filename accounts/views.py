from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login, authenticate
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
from accounts.models import CustomUser

def index(request):
    username = request.user.username
    return render(request, 'index.html',{"username":username})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request,"index.html")
        else:
            return render(request, 'index.html', {'error_message': 'Invalid username or password.'})
    else:
        return render(request, 'index.html')

def regist(request):
    if request.method == 'GET':
        return render(request, 'regist.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password1 = request.POST.get('password1', None)
        user = CustomUser.objects.create_user(username=username, password=password1)
    return redirect('index')

def manage(request):
    return render(request,"manage.html")

def detail(request):
    return render(request,"detail.html")

def mypage(request):
    return render(request,"mypage.html")