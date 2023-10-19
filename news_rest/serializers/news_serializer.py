from rest_framework import serializers
from news.models.news_model import News

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ["id", "title", "content", "author", "created_at", "image", "categories"]