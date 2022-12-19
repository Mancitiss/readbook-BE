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
router.register('story-new', views.Story_newViewSet)
router.register('list-story-new', views.List_story_newViewSet)
router.register('get_chapter/(?P<story_id>\w+)', views.Get_ChapterViewSet)

router.register('searchcategory/(?P<searchkey>\w+)', api.SearchCategory)
router.register('searstoryname/(?P<searchkey>\w+)', api.SearchStoryName)
router.register('get-story-catagory/(?P<story_id>\w+)', views.Get_Story_CatagoryViewSet)
router.register('get-story-history/(?P<story_id>\w+)', views.Get_Story_HistoryViewSet)


urlpatterns = [
    path('', include(router.urls)),
]