from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('categorys', views.CategoryViewSet)
router.register('users', views.UserViewSet)
router.register('bookreview/(?P<store_id>\w+)', views.BookReviewViewSet)
router.register('story', views.StoreReviewViewSet)
router.register('chapter/(?P<id>\d+)/(?P<chapter_id>\w+)', views.ChapterReviewViewSet)
router.register('chapter', views.ChapterReviewViewSetall)
router.register('story', views.StoryViewSet)
router.register('savestory', views.SaveStoryViewSet)

router.register('story-new', views.Story_newViewSet)
router.register('list-story-new', views.List_story_newViewSet)
router.register('get_chapter/(?P<story_id>\w+)', views.Get_ChapterViewSet)
router.register('history', views.HistoryViewSet)
router.register('searchcategory/(?P<searchkey>\w+)', views.SearchCategory)
router.register('searstoryname/(?P<searchkey>\w+)', views.SearchStoryName)
router.register('get-story-catagory/(?P<story_id>\w+)', views.Get_Story_CatagoryViewSet)
router.register('get-story-history/(?P<story_id>\w+)', views.Get_Story_HistoryViewSet)
router.register('my-book/(?P<story_id>\w+)', views.My_bookViewSet)
router.register('my-save/(?P<story_id>\w+)', views.My_saveViewSet)




urlpatterns = [
    path('', include(router.urls)),
]