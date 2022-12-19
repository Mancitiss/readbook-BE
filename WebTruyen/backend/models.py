from ctypes import addressof
from email.policy import default
from enum import unique
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    nickname = models.CharField(max_length=255, null=True)
    avatar = models.ImageField(upload_to='uploads/%Y/%m', null=True)
    intro = models.CharField(max_length=255, null=True)
    address = models.TextField(null=True, blank=True)
    hobbies = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True)


class Category(models.Model):

    category_name = models.CharField(max_length=255, null=False, unique=True)
    # category_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.category_name


class Story(models.Model):
    story_name = models.CharField(max_length=255, null=False)
    category_name = models.ManyToManyField('Category', blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=255, null=False)
    image = models.ImageField(upload_to='uploads/%Y/%m', blank=True, null=True)
    total_chapters = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    showtimes = models.TextField(null=True, blank=True)
    rating = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    views = models.IntegerField(default=0)
    introduce = models.TextField(null=True, blank=True)



class Chapter(models.Model):
    index = models.IntegerField(default=0)
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    chapter_name = models.CharField(max_length=255, null=False)
    content = models.TextField(null=True, blank=True)


class SaveStory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    previous_comment = models.ForeignKey(
        'Comment', on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)


class History(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)


class LoveComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    like_dislike = models.BooleanField(default=0)


class BookReview(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default=0)

class CaBook(models.Model):
    story_id = models.IntegerField(default=0)
    category_id = models.IntegerField(default=0)
