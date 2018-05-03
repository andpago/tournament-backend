from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Task(models.Model):
    # users cannot really be deleted, so this setting is irrelevant
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    text = models.TextField()  # for now this will be just text


class Solution(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    correct = models.NullBooleanField(null=True)  # null until checked
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
