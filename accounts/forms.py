#入力フォームを実装するところ
from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUser

class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1','password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)