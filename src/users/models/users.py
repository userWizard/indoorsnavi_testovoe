from django.db import models

from src.common.models import TimedBaseModel


class UserModel(TimedBaseModel):
    '''Model for users.'''
    username = models.CharField(
        verbose_name='Username',
        max_length=25,
        unique=True,
        blank=False,
        null=False,
    )
    email = models.EmailField(
        verbose_name='Email',
        max_length=254,
        unique=True,
        blank=False,
    )

    def __str__(self) -> str:
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
