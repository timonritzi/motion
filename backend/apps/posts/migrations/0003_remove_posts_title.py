# Generated by Django 3.1.2 on 2020-10-22 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20201021_1018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='title',
        ),
    ]
