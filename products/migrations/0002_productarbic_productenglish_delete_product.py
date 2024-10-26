# Generated by Django 5.1.1 on 2024-10-19 14:15

import products.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductArbic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('desc', models.TextField()),
                ('content', models.TextField(verbose_name='Content EN')),
                ('image', models.ImageField(blank=True, null=True, upload_to=products.utils.upload_image_product, verbose_name='Image')),
                ('status', models.BooleanField(default=True, verbose_name='Is Active?')),
            ],
            options={
                'verbose_name': 'Product Arbic',
                'verbose_name_plural': 'Products Arbic',
            },
        ),
        migrations.CreateModel(
            name='ProductEnglish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('desc', models.TextField()),
                ('content', models.TextField(verbose_name='Content EN')),
                ('image', models.ImageField(blank=True, null=True, upload_to=products.utils.upload_image_product, verbose_name='Image')),
                ('status', models.BooleanField(default=True, verbose_name='Is Active?')),
            ],
            options={
                'verbose_name': 'Product English',
                'verbose_name_plural': 'Products English',
            },
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]