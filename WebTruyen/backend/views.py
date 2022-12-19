from django.shortcuts import render
from rest_framework import viewsets, permissions, generics,response
from rest_framework.decorators import action
from .models import Category, User, Story, Chapter, CaBook
from .serializers import CategorySerializer, UserSerializer, StorySerializer, ChapterSerializer, CaBookSerializer
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from django.db.models.expressions import RawSQL

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
        return Story.objects.raw('SELECT id from backend_story order by id desc limit 20')

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
        return Story.objects.raw('SELECT s.id from backend_story_category_name as c, backend_story as s where category_id = ' + obj_id + ' and c.story_id = s.id order by s.id desc  limit 30')


class Get_Story_HistoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects
    serializer_class = StorySerializer 
    def get_queryset(self):
        obj_id = self.kwargs['story_id']
        return Story.objects.raw('SELECT s.id  from backend_history as h, backend_story as s where h.user_id = ' + obj_id +' and h.story_id = s.id order by s.id desc limit 1')