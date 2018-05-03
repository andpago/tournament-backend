from django.db import models


class Round(models.Model):
    title = models.TextField(max_length=255)
    is_deleted = models.BooleanField(default=False)

