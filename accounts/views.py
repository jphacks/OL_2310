from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login, authenticate
from django.http import JsonResponse
from accounts.forms import LoginForm,RegistrationForm

def index(request):
    username = request.user.username
    return render(request, 'index.html',{"username":username})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, "login.html",{'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def manage(request):
    return render(request, 'manage.html')