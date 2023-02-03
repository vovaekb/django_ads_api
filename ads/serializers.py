from ads.models import Ad
from rest_framework import serializers

class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ('title', 'text', 'status', 'created_at')