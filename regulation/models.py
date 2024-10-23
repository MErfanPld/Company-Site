from django.db import models
from .utils import *

# Create your models here.


class SettingsEnglish(models.Model):
    phone = models.CharField(max_length=20, verbose_name="Phone")
    email = models.EmailField(verbose_name="Email")
    address = models.TextField(verbose_name="Address")
    logo = models.ImageField(
        upload_to=upload_image_setting, null=True, blank=True, verbose_name='Logo')

    class Meta:
        verbose_name = 'Setting English'
        verbose_name_plural = 'Settings English'

    def __str__(self):
        return f"{self.phone} | {self.email}"

class SettingsArabic(models.Model):
    phone = models.CharField(max_length=20, verbose_name="Phone")
    email = models.EmailField(verbose_name="Email")
    address = models.TextField(verbose_name="Address")
    logo = models.ImageField(
        upload_to=upload_image_setting, null=True, blank=True, verbose_name='Logo')

    class Meta:
        verbose_name = 'Setting Arabic'
        verbose_name_plural = 'Settings Arabic'

    def __str__(self):
        return f"{self.phone} | {self.email}"


class Social(models.Model):
    link = models.URLField(verbose_name="Link")
    logo = models.ImageField(
        upload_to=upload_image_social, null=True, blank=True, verbose_name='Logo')

    class Meta:
        verbose_name = 'Social'
        verbose_name_plural = 'Social'

    def __str__(self):
        return f"{self.link}"
