from rest_framework import viewsets
from news.models.user_model import Users
from news_rest.serializers.users_serializer import UsersSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer