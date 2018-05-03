from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Tournament(models.Model):
    title = models.TextField(max_length=255)
    is_deleted = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Round(models.Model):
    title = models.TextField(max_length=255)
    is_deleted = models.BooleanField(default=False)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)