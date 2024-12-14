from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(
        'Email',
        unique=True,
        error_messages={
            'unique': "Пользователь с таким Email уже существует."
        }
    )
    avatar = models.ImageField(
        'Аватар',
        upload_to='avatars/',
        null=True,
        blank=True,
    )
    bio = models.TextField(
        'О себе',
        max_length=500,
        blank=True,
    )

    # Указываем, что для входа будет использоваться email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


    def __str__(self):
        return self.email