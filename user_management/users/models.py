# users/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

# Модель пользователя с расширением стандартной модели AbstractUser
class CustomUser(AbstractUser):
    # добавим дополнительные поля, если необходимо
    age = models.PositiveIntegerField(null=True, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.username
