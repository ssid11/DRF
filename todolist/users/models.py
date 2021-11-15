from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(verbose_name="Адрес электронной почты", unique=True,
                              help_text="Обязательное поле. Должно быть уникальным")
