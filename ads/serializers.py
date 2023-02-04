from ads.models import Ad, User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'is_staff')

class AdSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    class Meta:
        model = Ad
        fields = ('title', 'description', 'category', 'status', 'created_at', 'author')