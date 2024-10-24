from django.db import models

from aboutus.utils import *

# Create your models here.


class AchievementEnglish(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    content = models.TextField(verbose_name="Content")
    image = models.ImageField(
        upload_to=upload_image_achievement, null=True, blank=True, verbose_name='Image')
    status = models.BooleanField(
        default=True, verbose_name='Is Active?')

    class Meta:
        verbose_name = 'Achievement English'
        verbose_name_plural = 'Achievement English'

    def __str__(self):
        return f"{self.title} | {self.image} | {self.status}"


class AchievementArabic(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    content = models.TextField(verbose_name="Content")
    image = models.ImageField(
        upload_to=upload_image_achievement, null=True, blank=True, verbose_name='Image')
    status = models.BooleanField(
        default=True, verbose_name='Is Active?')

    class Meta:
        verbose_name = 'Achievement Arabic'
        verbose_name_plural = 'Achievement Arabic'

    def __str__(self):
        return f"{self.title} | {self.image} | {self.status}"


class TeamEnglish(models.Model):
    fullname = models.CharField(max_length=255)
    skill = models.CharField(max_length=500)
    image = models.ImageField(
        upload_to=upload_image_team, null=True, blank=True, verbose_name='Image')

    class Meta:
        verbose_name = 'Team English'
        verbose_name_plural = 'Team English'

    def __str__(self):
        return f"{self.fullname} | {self.image}"


class TeamArabic(models.Model):
    fullname = models.CharField(max_length=255)
    skill = models.CharField(max_length=500)
    image = models.ImageField(
        upload_to=upload_image_team, null=True, blank=True, verbose_name='Image')

    class Meta:
        verbose_name = 'Team Arabic'
        verbose_name_plural = 'Team Arabic'

    def __str__(self):
        return f"{self.fullname} | {self.image}"
