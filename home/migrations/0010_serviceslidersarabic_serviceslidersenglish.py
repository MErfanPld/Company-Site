# Generated by Django 5.1.1 on 2024-10-26 10:39

import home.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_remove_slidersarabic_title_ar_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceSlidersArabic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('sub_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Sub Title')),
                ('image', models.ImageField(blank=True, null=True, upload_to=home.utils.upload_image_sliders, verbose_name='Image')),
                ('status', models.BooleanField(default=True, verbose_name='Is Active?')),
            ],
            options={
                'verbose_name': 'Service Slider Arabic',
                'verbose_name_plural': 'Service Sliders Arabic',
            },
        ),
        migrations.CreateModel(
            name='ServiceSlidersEnglish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('sub_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Sub Title')),
                ('image', models.ImageField(blank=True, null=True, upload_to=home.utils.upload_image_sliders, verbose_name='Image')),
                ('status', models.BooleanField(default=True, verbose_name='Is Active?')),
            ],
            options={
                'verbose_name': 'Service Slider English',
                'verbose_name_plural': 'Service Sliders English',
            },
        ),
    ]