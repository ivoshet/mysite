# Generated by Django 4.0.4 on 2022-05-10 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_games_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='file',
            field=models.FileField(upload_to='upload', verbose_name='Файл'),
        ),
    ]
