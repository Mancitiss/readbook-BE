
from rest_framework.serializers import ModelSerializer
from .models import Category, User, Story, Chapter

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'password', 'avatar','nickname', 'intro', 'hobbies','address', 'phone']
        extra_kwargs = {
            'password': {'write_only': 'true'}
        }

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ["category_name"]

class StorySerializer(ModelSerializer):
    class Meta:
        model = Story
        fields = ["story_name", "category_name", "create_date", "author", "image", "total_chapters", "user", "showtimes", "rating", "views", "introduce"]


class ChapterSerializer(ModelSerializer):
    class Meta:
        model = Chapter
        fields = ["index", "story", "chapter_name", "content"]