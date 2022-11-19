
from rest_framework.serializers import ModelSerializer
from .models import Category, User

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