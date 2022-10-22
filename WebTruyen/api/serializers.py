from rest_framework import serializers
from backend.models import Story,Chapter


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ('id',
                  'story',
                  'chapter_name',
                  'content')
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


