from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

#ユーザーアカウント
class CustomUser(AbstractUser):
    groups = models.ManyToManyField('auth.Group', related_name='custom_user_groups')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_permissions')

#本
class Book(models.Model):
    title = models.CharField(max_length=100)
    is_borrowed = models.BooleanField(default=False)
    lend_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

#タグ
class Tag(models.Model):
    name = models.CharField(max_length=50)
    books = models.ManyToManyField(Book)