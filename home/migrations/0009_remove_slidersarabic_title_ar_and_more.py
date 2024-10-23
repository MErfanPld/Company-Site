# Generated by Django 5.1.1 on 2024-10-23 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_aboutusarabic_aboutusenglish_chooseusarabic_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slidersarabic',
            name='title_ar',
        ),
        migrations.AlterField(
            model_name='slidersarabic',
            name='sub_title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Sub Title'),
        ),
        migrations.AlterField(
            model_name='slidersarabic',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Title'),
        ),
    ]
