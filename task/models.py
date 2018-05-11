from django.contrib.auth import get_user_model
from django.db import models

from round.models import Round

User = get_user_model()


class Task(models.Model):
    # users cannot really be deleted, so this setting is irrelevant
    title = models.TextField(max_length=255)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    text = models.TextField()  # for now this will be just text
    # again, these things cannot be deleted
    round = models.ForeignKey(Round, on_delete=models.CASCADE, related_name='tasks')
    is_deleted = models.BooleanField(default=False)
    answer = models.TextField()


class Solution(models.Model):  # a rare example of a deletable object
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    correct = models.NullBooleanField(null=True)  # null until checked
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='solutions')

    def check_solution(self):
        return self.text == self.task.answer
