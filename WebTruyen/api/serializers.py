from rest_framework import serializers
from backend.models import Story,Chapter,Category,Category, User,BookReview
from rest_framework.serializers import ModelSerializer
class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'
class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ('id',
                  'category_name',
                  'story_name',
                  'create_date',
                  'author',
                  'image',
                  'total_chapters',
                  'user',
                  'showtimes',
                  'rating',
                  'views',
                  'introduce'
                  )
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
class BookreviewSerializer(ModelSerializer):
    class Meta:
        model = BookReview
        fields = ["story","user","content","create_date","like"]

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
