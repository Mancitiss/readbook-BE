from django.shortcuts import render
from rest_framework import viewsets, permissions, generics,response
from rest_framework.decorators import action
from .models import Category, User, Story, Chapter
from .serializers import CategorySerializer, UserSerializer, StorySerializer, ChapterSerializer
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response


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

class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.filter()
    serializer_class = ChapterSerializer