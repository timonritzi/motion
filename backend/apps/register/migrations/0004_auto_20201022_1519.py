# Generated by Django 3.1.2 on 2020-10-22 15:19

import apps.register.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_auto_20201022_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='code',
            field=models.CharField(default=apps.register.models.code_generator, max_length=6),
        ),
    ]
