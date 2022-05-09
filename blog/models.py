from tabnanny import verbose
from django.db import models
from django.conf import settings
from django.utils import timezone

class Games(models.Model):
    title = models.CharField(max_length=250, verbose_name='Наименование')
    # to upload file in directory /upload
    file = models.FileField(upload_to='upload', verbose_name='Файл')
    counter = models.PositiveIntegerField(default=0, verbose_name='Количество загрузок')
    created = models.DateTimeField(default=timezone.now, verbose_name='Создан')

    def __str__(self):
        return self.title

    class Meta:
        verbose = 'Игра'
        verbose_name_plural = 'Игры'
        ordering = ['-created']