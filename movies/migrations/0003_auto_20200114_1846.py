# Generated by Django 3.0 on 2020-01-14 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20200114_1839'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MoviesShots',
            new_name='MovieShots',
        ),
    ]
