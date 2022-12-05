from django.urls import path, include
from . import views
from api import views as api
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('categorys', api.CategoryViewSet)
router.register('users', api.UserViewSet)
router.register('bookreview/(?P<store_id>\w+)', api.BookReviewViewSet)
router.register('story', api.StoreReviewViewSet)
router.register('chapter/(?P<id>\d+)/(?P<chapter_id>\w+)', api.ChapterReviewViewSet)
router.register('chapter', api.ChapterReviewViewSetall)
router.register('story', views.StoryViewSet)
urlpatterns = [
    path('', include(router.urls)),
]