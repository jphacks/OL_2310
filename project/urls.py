#urlパターンを実装するところ

from django.contrib import admin
from django.urls import path
from accounts.views import index,user_login,regist,detail,manage,mypage
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index,name="index"),
    path("login/",user_login,name="login"),
    path("regist/",regist,name="regist"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('detail/',detail,name="detail"),
    path("manage/",manage, name="manage"),
    path("mypage/",mypage,name="mypage"),
]