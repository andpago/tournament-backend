"""tournament URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from app.views import UserViewSet
from news.views import PostListViewSet
from round.views import TournamentViewSet, RoundViewSet
from task.views import TaskViewSet, SolutionViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, 'users')
router.register(r'tournaments', TournamentViewSet, 'tournaments')
router.register(r'rounds', RoundViewSet, 'rounds')
router.register(r'tasks', TaskViewSet, 'tasks')
router.register(r'solutions', SolutionViewSet, 'solutions')
router.register(r'news', PostListViewSet, 'news')

urlpatterns = [
    path('api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
