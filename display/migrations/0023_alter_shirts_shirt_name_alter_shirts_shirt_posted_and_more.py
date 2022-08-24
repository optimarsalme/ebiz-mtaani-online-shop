# Generated by Django 4.1 on 2022-08-19 04:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0022_alter_shirts_shirt_posted_alter_shoes_shoe_posted_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shirts',
            name='shirt_name',
            field=models.CharField(default='Casual', max_length=20, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='shirts',
            name='shirt_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 19, 7, 32, 6, 139574), verbose_name='date posted'),
        ),
        migrations.AlterField(
            model_name='shoes',
            name='shoe_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 19, 7, 32, 6, 139574), verbose_name='date posted'),
        ),
        migrations.AlterField(
            model_name='sweaters',
            name='sweater_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 19, 7, 32, 6, 139574), verbose_name='date posted'),
        ),
    ]
