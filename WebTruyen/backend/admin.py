from django.contrib import admin
from .models import History, Comment, LoveStory, Chapter, Story, Category, User
# Register your models here.
admin.site.register(History)
admin.site.register(Comment)
admin.site.register(LoveStory)
admin.site.register(Chapter)
admin.site.register(Story)
admin.site.register(Category)
admin.site.register(User)

