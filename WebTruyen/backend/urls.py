from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('categorys', views.CategoryViewSet)
router.register('users', views.UserViewSet)
router.register('story', views.StoryViewSet)
router.register('chapter', views.ChapterViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
