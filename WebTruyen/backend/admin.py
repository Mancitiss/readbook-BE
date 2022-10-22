from django.contrib import admin
from .models import History, Comment, SaveStory, Chapter, Story, Category, User, LoveComment, BookReview
# Register your models here.
admin.site.register(History)
admin.site.register(Comment)
admin.site.register(SaveStory)
admin.site.register(Chapter)
admin.site.register(Story)
admin.site.register(Category)
admin.site.register(User)
admin.site.register(BookReview)
admin.site.register(LoveComment)
