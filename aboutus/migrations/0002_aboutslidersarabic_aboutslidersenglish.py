# Generated by Django 5.1.1 on 2024-10-26 10:39

import aboutus.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutSlidersArabic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('sub_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Sub Title')),
                ('image', models.ImageField(blank=True, null=True, upload_to=aboutus.utils.upload_image_sliders, verbose_name='Image')),
                ('status', models.BooleanField(default=True, verbose_name='Is Active?')),
            ],
            options={
                'verbose_name': 'About Us Slider Arabic',
                'verbose_name_plural': 'About Us Sliders Arabic',
            },
        ),
        migrations.CreateModel(
            name='AboutSlidersEnglish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('sub_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Sub Title')),
                ('image', models.ImageField(blank=True, null=True, upload_to=aboutus.utils.upload_image_sliders, verbose_name='Image')),
                ('status', models.BooleanField(default=True, verbose_name='Is Active?')),
            ],
            options={
                'verbose_name': 'About Us Slider English',
                'verbose_name_plural': 'About Us Sliders English',
            },
        ),
    ]
