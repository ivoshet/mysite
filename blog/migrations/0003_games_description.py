# Generated by Django 4.0.4 on 2022-05-09 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_games_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
