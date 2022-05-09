from tabnanny import verbose
from django.db import models
from django.conf import settings
from django.utils import timezone

# python manage.py makemigrations blog
# python manage.py migrate
# python manage.py runserver

class Games(models.Model):
    title = models.CharField(max_length=250, verbose_name='Наименование')

    # to upload file in directory blog/upload

    file = models.FileField(upload_to='blog/upload', verbose_name='Файл')
    counter = models.PositiveIntegerField(default=0, verbose_name='Количество загрузок')
    created = models.DateTimeField(default=timezone.now, verbose_name='Создан')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'
        ordering = ['-created']