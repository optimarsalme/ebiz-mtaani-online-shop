# Generated by Django 4.1 on 2022-08-17 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shirts',
            name='name',
            field=models.CharField(default='Casual', max_length=20),
        ),
        migrations.AlterField(
            model_name='shirts',
            name='price',
            field=models.CharField(default='200', max_length=200),
        ),
        migrations.AlterField(
            model_name='sweaters',
            name='name',
            field=models.CharField(default='Casual', max_length=20),
        ),
        migrations.AlterField(
            model_name='sweaters',
            name='price',
            field=models.TextField(default='200', max_length=200),
        ),
    ]
