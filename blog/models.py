from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models
from django.conf import settings
from django.utils import timezone

# python manage.py makemigrations blog
# python manage.py migrate
# python manage.py runserver

class Games(models.Model):
    title = models.CharField(max_length=250, verbose_name='Наименование')

    # IVOSHET: to upload file in directory blog/upload

    file = models.FileField(upload_to="upload", verbose_name='Файл')
    description = models.TextField()
    counter = models.PositiveIntegerField(default=0, verbose_name='Количество загрузок')
    created = models.DateTimeField(default=timezone.now, verbose_name='Создан')
    # IVOSHET: for upload and show icons of apps
    image = models.FileField(upload_to="upload", verbose_name='картинка')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'
        ordering = ['-created']