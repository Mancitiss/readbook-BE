from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.decorators import action
from .models import Category, User, Story, Chapter, History, SaveStory, BookReview
from .serializers import CategorySerializer, UserSerializer, StorySerializer, ChapterSerializer, HistorySerializer, SaveStorySerializer, BookreviewSerializer
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

# Create your views here.

class UserViewSet(viewsets.ViewSet, generics.ListAPIView , generics.CreateAPIView, generics.RetrieveAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser]

    # def get_permissions(self):
    #     if self.action == 'current_user':
    #         return [permissions.IsAuthenticated()]
    #     if self.action == 'retrieve':
    #         return [permissions.IsAuthenticated()]
    #     return [permissions.AllowAny()]

    @action(methods=['get'], detail=False, url_path='current-user')
    def current_user(self, request):
        return Response(self.serializer_class(request.user).data)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter()
    serializer_class = CategorySerializer
    
class SaveStoryViewSet(viewsets.ModelViewSet):
    queryset = SaveStory.objects.filter()
    serializer_class = SaveStorySerializer

class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.filter()
    serializer_class = HistorySerializer

class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.filter()
    serializer_class = StorySerializer
class Story_newViewSet(viewsets.ModelViewSet):
    queryset = Story.objects
    serializer_class = StorySerializer 
    def get_queryset(self):
        return Story.objects.raw('SELECT id from backend_story order by id desc limit 1')

class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.filter()
    serializer_class = ChapterSerializer
class Get_ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.filter()
    serializer_class = ChapterSerializer 
    def get_queryset(self):
        obj_id = self.kwargs['story_id']
        return Chapter.objects.raw('SELECT * from backend_chapter where story_id = ' + obj_id + ' order by [index] desc')

class List_story_newViewSet(viewsets.ModelViewSet):
    queryset = Story.objects
    serializer_class = StorySerializer 
    def get_queryset(self):
        return Story.objects.raw('SELECT id from backend_story order by id desc limit 30')

# class Get_Story_CatagoryViewSet(viewsets.ModelViewSet):
#     queryset = CaBook.objects
#     serializer_class = CaBookSerializer 
#     def get_queryset(self):
#         obj_id = self.kwargs['story_id']
#         return Chapter.objects.raw('SELECT * from backend_story_category_name where category_id = ' + obj_id + ' order by id desc')

class Get_Story_CatagoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects
    serializer_class = StorySerializer 
    def get_queryset(self):
        obj_id = self.kwargs['story_id']
        return Story.objects.raw('SELECT s.id from backend_story_category_name as c, backend_story as s where category_id = ' + obj_id + ' and c.story_id = s.id order by s.id desc  limit 40')

class Get_Story_HistoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects
    serializer_class = StorySerializer 
    def get_queryset(self):
        obj_id = self.kwargs['story_id']
        return Story.objects.raw('SELECT DISTINCT s.id  from backend_history as h, backend_story as s where h.user_id = ' + obj_id +' and h.story_id = s.id order by s.id desc limit 8')

class My_bookViewSet(viewsets.ModelViewSet):
    queryset = Story.objects
    serializer_class = StorySerializer 
    def get_queryset(self):
        obj_id = self.kwargs['story_id']
        return Story.objects.raw('SELECT id from backend_story where user_id = ' + obj_id + ' order by id desc')      

class My_saveViewSet(viewsets.ModelViewSet):
    queryset = Story.objects
    serializer_class = StorySerializer 
    def get_queryset(self):
        obj_id = self.kwargs['story_id']
        return Story.objects.raw('SELECT * from backend_story where id in (select story_id from backend_savestory where user_id = ' + obj_id + ' order by id desc)')          
    
# new file

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 1000

class BookReviewViewSet(viewsets.ModelViewSet):

    queryset = BookReview.objects.filter()
    serializer_class = BookreviewSerializer

    def get_queryset(self):
        obj_id = self.kwargs['store_id']
        if obj_id != 'all':
            query = BookReview.objects.filter(story=obj_id)
        else:
            query = BookReview.objects.all()
        return query


class StoreReviewViewSet(viewsets.ModelViewSet):

    queryset = Story.objects.filter()
    serializer_class = StorySerializer


class ChapterReviewViewSet(viewsets.ModelViewSet):
   # pagination_class = StandardResultsSetPagination
    queryset = Chapter.objects.filter()
    serializer_class = ChapterSerializer

    def get_queryset(self):
        obj_id = self.kwargs['id']
        obj_id1 = self.kwargs['chapter_id']
        if obj_id:
            query = Chapter.objects.filter(story=obj_id)
        if obj_id1 != 'all':
            query = query.filter(id=obj_id1)
          #  if obj_id1:
           #
        # do something with data
        return query


class ChapterReviewViewSetall(viewsets.ModelViewSet):
   # pagination_class = StandardResultsSetPagination
   # pagination_class = StandardResultsSetPagination
    queryset = Chapter.objects.filter()
    serializer_class = ChapterSerializer


class SearchCategory(viewsets.ModelViewSet):
    queryset = Category.objects.filter()
    serializer_class = CategorySerializer
    def get_queryset(self):
        obj_id = self.kwargs['searchkey']
        print(obj_id)

        if obj_id:
            query = Category.objects.filter(category_name__contains=obj_id)
        else:
            query = Category.objects.all()
        return query
    
class SearchStoryName(viewsets.ModelViewSet):
    queryset = Story.objects.filter()
    serializer_class = StorySerializer
    def get_queryset(self):
        obj_id = self.kwargs['searchkey']
        print(obj_id)

        if obj_id:
            query = Story.objects.filter(story_name__contains=obj_id)
        else:
            query = Story.objects.all()
        return query
