#urlパターンを実装するところ
from django.contrib import admin
from django.urls import path
from accounts.views import top,create_bookshelf,index,user_login,regist,detail,setting,mypage,borrow_book,return_books,add_book,delete_book,edit_book,create_tag,attach_tag,delete_tag,untag_book,edit_tag
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",top,name="top"),
    path("index/",index,name="index"),
    path("create_bookshelf",create_bookshelf,name="create_bookshelf"4),
    path("login/",user_login,name="login"),
    path("regist/",regist,name="regist"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('detail/<int:book_id>',detail,name="detail"),
    path("setting/",setting, name="setting"),
    path("add_book/",add_book,name="add_book"),
    path("delete_book/<int:book_id>",delete_book,name="delete_book"),
    path("edit_book/<int:book_id>",edit_book,name="edit_book"),
    path("create_tag/",create_tag,name="create_tag"),
    path("attach_tag/<int:book_id>",attach_tag,name="attach_tag"),
    path("delete_tag/<int:tag_id>",delete_tag,name="delete_tag"),
    path("edit_tag/<int:tag_id>",edit_tag,name="edit_tag"),
    path("untag_book/<int:book_id>",untag_book,name="untag_book"),
    path("mypage/",mypage,name="mypage"),
    path("borrow_book/<int:book_id>",borrow_book,name="borrow_book"),
    path('return/',return_books, name='return_books'),
]