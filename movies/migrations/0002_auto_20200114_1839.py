# Generated by Django 3.0 on 2020-01-14 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actor',
            old_name='descriptions',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='descriptions',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='genre',
            old_name='descriptions',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='descriptions',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='moviesshots',
            old_name='descriptions',
            new_name='description',
        ),
    ]
