# Generated by Django 4.1 on 2023-04-11 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0002_fotografia_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='publicada',
            field=models.BooleanField(default=False),
        ),
    ]
