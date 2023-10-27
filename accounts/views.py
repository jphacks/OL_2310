from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login, authenticate
from django.http import HttpResponse,JsonResponse
from accounts.models import CustomUser,UserProfile,Book
from django.contrib.auth.decorators import login_required

def index(request):
    username = request.user.username
    books = Book.objects.all
    return render(request, 'index.html',{"username":username,"books":books})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return redirect("user_login",{"error_mesage":"ユーザーネームもしくはパスワードが間違っています"})
    else:
        return render(request, 'login.html')

def regist(request):
    if request.method == 'GET':
        return render(request, 'regist.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password1 = request.POST.get('password1', None)
        user = CustomUser.objects.create_user(username=username, password=password1)
        profile = UserProfile(user=user)
        profile.save()
    return redirect('index')

@login_required
def manage(request):
    books = Book.objects.all
    if request.method =='POST':
        title = request.POST.get('title',None)
        book = Book(title=title)
        book.save()
        return redirect("manage")
    return render(request,"manage.html",{"books":books})

def detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request,"detail.html",{"book":book})

@login_required
def borrow_book(request,book_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            book = get_object_or_404(Book,id=book_id)
            user_profile = UserProfile.objects.get(user=request.user)
            book.is_borrowed = True
            book.save()
            user_profile.borrowed_books.add(book)
            return redirect("detail",book_id=book_id)
    else:
        return redirect("login")

@login_required
def return_books(request):
    if request.method == 'POST':
        book_ids = request.POST.getlist('return_checkbox')
        user_profile = UserProfile.objects.get(user=request.user)
        for book_id in book_ids:
            book = Book.objects.get(id=book_id)
            if book in user_profile.borrowed_books.all():
                book.is_borrowed = False
                book.save()
                user_profile.borrowed_books.remove(book)
    return redirect('mypage')

@login_required
def mypage(request):
    username = request.user.username
    user_profile=UserProfile.objects.get(user=request.user)
    borrowed_books = user_profile.borrowed_books.all()
    return render(request,"mypage.html" ,{"username":username,"borrowed_books":borrowed_books})