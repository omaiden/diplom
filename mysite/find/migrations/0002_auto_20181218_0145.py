# Generated by Django 2.1.4 on 2018-12-17 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('find', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relative',
            name='birthday',
        ),
        migrations.RemoveField(
            model_name='relative',
            name='nickname',
        ),
        migrations.RemoveField(
            model_name='relative',
            name='position',
        ),
        migrations.RemoveField(
            model_name='relative',
            name='relation',
        ),
    ]