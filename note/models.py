from django.db import models


class Note(models.Model):
    name = models.CharField(verbose_name='Заголовок', max_length=128)
    content = models.TextField(verbose_name='Содержание')

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
        ordering = ['-id']

    def __str__(self):
        return self.name
