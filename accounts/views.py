from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login, authenticate
from django.http import HttpResponse,JsonResponse
from accounts.models import CustomUser,UserProfile,Book,Tag
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
def setting(request):
    books = Book.objects.all()
    tags = Tag.objects.all()
    return render(request,"setting.html",{"books":books,"tags":tags})

@login_required
def add_book(request):
    if request.method =='POST':
        title = request.POST.get('title',None)
        book = Book(title=title)
        book.save()
        return redirect("setting")

@login_required
def delete_book(request, book_id):
    if request.method == 'POST':
        book = Book.objects.get(id=book_id)
        book.delete()
        return redirect('setting')

@login_required
def edit_book(request,book_id):
    book = Book.objects.get(id=book_id)
    if request.method == "POST":
        new_title = request.POST.get('title',None)
        book.title = new_title
        book.save()
        return redirect("setting")

@login_required
def create_tag(request):
    tag_name = request.POST.get('tag_name',None)
    tag = Tag(name=tag_name)
    tag.save()
    return redirect("setting")

@login_required
def attach_tag(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        tag_id = request.POST.get('tag_id')
        tag = Tag.objects.get(id=tag_id)
        book.tags.add(tag)
        return redirect("setting")

@login_required
def edit_tag(request,tag_id):
    tag = Tag.objects.get(id=tag_id)
    if request.method == "POST":
        new_name = request.POST.get('name',None)
        tag.name = new_name
        tag.save()
        return redirect("setting")

@login_required
def delete_tag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    if request.method == 'POST':
        tag.delete()
        return redirect('setting')

@login_required
def untag_book(request, book_id):
    if request.method == 'POST':
        book = Book.objects.get(id=book_id)
        selected_tags = request.POST.getlist('tag_id')
        for tag_id in selected_tags:
            tag = Tag.objects.get(id=tag_id)
            book.tags.remove(tag)
    return redirect('setting')

def detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request,"detail.html",{"book":book})

@login_required
def borrow_book(request,book_id):
    if request.method == 'POST':
        book = get_object_or_404(Book,id=book_id)
        user_profile = UserProfile.objects.get(user=request.user)
        book.is_borrowed = True
        book.save()
        user_profile.borrowed_books.add(book)
        return redirect("detail",book_id=book_id)

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