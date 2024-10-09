# Generated by Django 5.1.1 on 2024-09-27 08:19

import regulation.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regulation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=regulation.utils.upload_image_social, verbose_name='Logo'),
        ),
    ]