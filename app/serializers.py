from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ('email', 'username')

