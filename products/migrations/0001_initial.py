# Generated by Django 5.1.1 on 2024-10-18 10:50

import products.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_en', models.CharField(max_length=255)),
                ('title_ar', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('desc_en', models.TextField()),
                ('desc_ar', models.TextField()),
                ('content_en', models.TextField(verbose_name='Content EN')),
                ('content_ar', models.TextField(verbose_name='Content AR')),
                ('image', models.ImageField(blank=True, null=True, upload_to=products.utils.upload_image_product, verbose_name='Image')),
                ('status', models.BooleanField(default=True, verbose_name='Is Active?')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
