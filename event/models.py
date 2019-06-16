from django.db import models
from django.utils import timezone


class Event(models.Model):
    created = models.DateTimeField(verbose_name='Время создания', default=timezone.now())
    name = models.CharField(verbose_name='Название события', max_length=128)
    description = models.TextField(verbose_name='Описание')
    end_date = models.DateTimeField(verbose_name='Дата окончания события')

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
        ordering = ['end_date']

    def __str__(self):
        return self.name

