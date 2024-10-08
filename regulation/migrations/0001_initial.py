# Generated by Django 5.1.1 on 2024-09-17 08:45

import regulation.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20, verbose_name='Phone')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('address', models.TextField(verbose_name='Address')),
                ('logo', models.ImageField(blank=True, null=True, upload_to=regulation.utils.upload_image_setting, verbose_name='Logo')),
            ],
            options={
                'verbose_name': 'Setting',
                'verbose_name_plural': 'Settings',
            },
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(verbose_name='Link')),
                ('logo', models.ImageField(blank=True, null=True, upload_to=regulation.utils.upload_image_setting, verbose_name='Logo')),
            ],
            options={
                'verbose_name': 'Social',
                'verbose_name_plural': 'Social',
            },
        ),
    ]
