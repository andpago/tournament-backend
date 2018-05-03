from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Task(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL) # users cannot really be deleted
    text = models.TextField() # for now this will be just text
