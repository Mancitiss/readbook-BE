from ctypes import addressof
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(upload_to='uploads/%Y/%m')
    intro = models.CharField(max_length=255, null=True)
    nickname = models.CharField(max_length=255, null=True)
    address = models.TextField(null=True, blank=True)
    hobbies = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True)
class Category(models.Model):
    # tl_id
    category_name = models.CharField(max_length=255, null=False)
    def __str__(self):
        return self.category_name
    
class Story(models.Model):
    # tr_id 
    category_name = models.ManyToManyField('Category', blank=True, null=True)
    story_name = models.CharField(max_length=255, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=255, null=False)
    image = models.ImageField(upload_to='uploads/%Y/%m')
    total_chapters = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    showtimes = models.TextField(null=True, blank=True)
    likes = models.IntegerField()
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    views = models.IntegerField()
    introduce = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.category_name

class Chapter(models.Model):
    # ch_id
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chapter_name = models.CharField(max_length=255, null=False)
    content = models.TextField(null=True, blank=True)

class LoveStory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    # bl_id 
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)

class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    story = models.ForeignKey(Story, on_delete=models.CASCADE)