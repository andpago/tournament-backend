from django.contrib.auth import get_user_model
from rest_framework import viewsets

from app.serializers import UserSerializer

User = get_user_model()


class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
