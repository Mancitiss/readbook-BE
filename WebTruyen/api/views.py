from django.shortcuts import render

from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import action
from backend.models import Chapter, Story, Category, User, BookReview
from api.serializers import ChapterSerializer, StorySerializer, CategorySerializer, UserSerializer, BookreviewSerializer
from rest_framework.decorators import api_view
from rest_framework import viewsets, permissions, generics, response
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import filters


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 1000


class UserViewSet(viewsets.ViewSet, generics.ListAPIView, generics.CreateAPIView, generics.RetrieveAPIView):
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
