# Generated by Django 4.0.4 on 2022-05-09 11:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Наименование')),
                ('file', models.FileField(upload_to='upload', verbose_name='Файл')),
                ('counter', models.PositiveIntegerField(default=0, verbose_name='Количество загрузок')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Создан')),
            ],
            options={
                'verbose_name': 'Игра',
                'verbose_name_plural': 'Игры',
                'ordering': ['-created'],
            },
        ),
    ]