#urlパターンを実装するところ
from django.contrib import admin
from django.urls import path
from accounts.views import index,user_login,regist,detail,setting,mypage,borrow_book,return_books,add_book
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index,name="index"),
    path("login/",user_login,name="login"),
    path("regist/",regist,name="regist"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('detail/<int:book_id>',detail,name="detail"),
    path("setting/",setting, name="setting"),
    path("add_book/",add_book,name="add_book"),
    path("mypage/",mypage,name="mypage"),
    path("borrow_book/<int:book_id>",borrow_book,name="borrow_book"),
    path('return/',return_books, name='return_books'),
]