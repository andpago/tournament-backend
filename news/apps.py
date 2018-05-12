from django.apps import AppConfig
from django.contrib import admin

from news.models import Post


class NewsConfig(AppConfig):
    name = 'news'


class PostAdmin(admin.ModelAdmin):
    model = Post


admin.site.register(Post, PostAdmin)
