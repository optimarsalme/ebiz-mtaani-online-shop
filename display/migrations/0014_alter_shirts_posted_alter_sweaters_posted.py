# Generated by Django 4.1 on 2022-08-18 07:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0013_alter_shirts_posted_alter_sweaters_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shirts',
            name='posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 18, 10, 12, 41, 520834), verbose_name='date posted'),
        ),
        migrations.AlterField(
            model_name='sweaters',
            name='posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 18, 10, 12, 41, 519834), verbose_name='date posted'),
        ),
    ]
