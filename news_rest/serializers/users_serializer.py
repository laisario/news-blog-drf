from rest_framework import serializers
from news.models.user_model import Users

class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ["id", "name", "email", "role"]