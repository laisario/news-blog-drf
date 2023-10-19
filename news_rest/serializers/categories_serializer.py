from rest_framework import serializers
from news.models.category_model import Categories

class CategoriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categories
        fields = ["id", "name"]