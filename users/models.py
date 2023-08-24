from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=50, verbose_name='имя')
    last_name = models.CharField(max_length=35, verbose_name='фамилия')
    email = models.EmailField(unique=True, verbose_name='email')
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    chat_id = models.CharField(max_length=100, verbose_name='чат ID телеграмм', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
