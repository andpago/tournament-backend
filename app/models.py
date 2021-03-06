from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    is_deleted = models.BooleanField(default=False)
    bio = models.TextField()
    avatar = models.ImageField()

