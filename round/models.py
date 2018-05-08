from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Tournament(models.Model):
    title = models.TextField(max_length=255)
    is_deleted = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()


class Round(models.Model):
    title = models.TextField(max_length=255)
    is_deleted = models.BooleanField(default=False)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='rounds')
    participants = models.ManyToManyField(User, related_name='rounds')
    is_final = models.BooleanField(default=False)
    is_selection = models.BooleanField(default=False)

