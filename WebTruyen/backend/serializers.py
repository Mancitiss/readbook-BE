
from rest_framework.serializers import ModelSerializer
from .models import Category, User, Story, Chapter, CaBook, History, SaveStory

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
        fields = "__all__"

class Category1Serializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ["id"]

class StorySerializer(ModelSerializer):
    class Meta:
        model = Story
        fields = ["id", "story_name", "category_name", "create_date", "author", "image", "total_chapters", "user", "showtimes", "rating", "views", "introduce"]


class ChapterSerializer(ModelSerializer):
    class Meta:
        model = Chapter
        fields = "__all__"

class CaBookSerializer(ModelSerializer):
    class Meta:
        model = CaBook
        fields = "__all__"   

class HistorySerializer(ModelSerializer):
    class Meta:
        model = History
        fields = "__all__"

class SaveStorySerializer(ModelSerializer):
    class Meta:
        model = SaveStory
        fields = "__all__"
