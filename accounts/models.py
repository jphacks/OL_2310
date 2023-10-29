from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    groups = models.ManyToManyField('auth.Group', related_name='custom_user_groups')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_permissions')

class Book(models.Model):
    title = models.CharField(max_length=100)
    is_borrowed = models.BooleanField(default=False)
    tags = models.ManyToManyField('Tag', related_name='books', blank=True)

class Tag(models.Model):
    name = models.CharField(max_length=50)

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    borrowed_books = models.ManyToManyField(Book, blank=True,null=True)
