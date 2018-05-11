from django import http
from django.contrib.auth import get_user_model
from rest_framework import viewsets

from app.serializers import UserSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def get_user_info(request):
    ALLOWED_METHODS = ['GET']
    AUTH_HEADER = 'HTTP_AUTHORIZATION'
    TOKEN_PREFIX = 'Token '

    if request.method not in ALLOWED_METHODS:
        return http.HttpResponse(status=405)  # method not allowed

    headers = request.META

    if AUTH_HEADER not in headers:
        return http.HttpResponse(status=401)  # unauthorized

    token = headers[AUTH_HEADER]

    if not token.startswith(TOKEN_PREFIX):
        return http.HttpResponseBadRequest()

    token = token[len(TOKEN_PREFIX):]

    try:
        user = User.objects.get(auth_token=token)
        return http.JsonResponse(UserSerializer(user).data)
    except User.DoesNotExist:
        return http.HttpResponseNotFound()
