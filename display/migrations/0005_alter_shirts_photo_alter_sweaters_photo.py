# Generated by Django 4.1 on 2022-08-17 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0004_alter_shirts_photo_alter_sweaters_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shirts',
            name='photo',
            field=models.ImageField(blank=True, upload_to='Shirts/'),
        ),
        migrations.AlterField(
            model_name='sweaters',
            name='photo',
            field=models.ImageField(blank=True, upload_to='Sweater/'),
        ),
    ]
