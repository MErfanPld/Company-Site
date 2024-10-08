# Generated by Django 5.1.1 on 2024-09-16 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_service_icon_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='fullname',
        ),
        migrations.AddField(
            model_name='comments',
            name='fullname_ar',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Full Name AR'),
        ),
        migrations.AddField(
            model_name='comments',
            name='fullname_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Full Name EN'),
        ),
        migrations.AlterField(
            model_name='sliders',
            name='sub_title_ar',
            field=models.CharField(max_length=255, verbose_name='Sub Title AR'),
        ),
    ]
