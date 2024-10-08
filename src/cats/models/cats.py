from django.db import models

from src.common.models import TimedBaseModel
from src.users.models.users import UserModel


class CatsModel(TimedBaseModel):
    '''Model for cats.'''
    owner = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='cats',
        verbose_name='Owner',
    )
    name = models.CharField(
        verbose_name='Name',
        max_length=100,
        blank=False,
        null=False,
    )
    age = models.PositiveIntegerField(
        verbose_name='Age',
        blank=False,
        null=False,
    )
    breed = models.CharField(
        verbose_name='Breed',
        max_length=100,
        blank=True,
        null=True,
    )
    hairines = models.CharField(
        verbose_name='Hairines',
        max_length=100,
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        return f'{self.name} {self.breed} {self.hairines}'

    class Meta:
        verbose_name = 'Cat'
        verbose_name_plural = 'Cats'
