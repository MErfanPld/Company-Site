from django.db import models

from news.utils import upload_image_news

# Create your models here.

class NewsEnglish(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(verbose_name="Content EN")
    image = models.ImageField(
        upload_to=upload_image_news, null=True, blank=True, verbose_name='Image')
    status = models.BooleanField(
        default=True, verbose_name='Is Active?')

    class Meta:
        verbose_name = 'New English'
        verbose_name_plural = 'News English'

    def __str__(self):
        return f"{self.title} | {self.image} | {self.status}"

class NewsArabic(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(verbose_name="Content EN")
    image = models.ImageField(
        upload_to=upload_image_news, null=True, blank=True, verbose_name='Image')
    status = models.BooleanField(
        default=True, verbose_name='Is Active?')

    class Meta:
        verbose_name = 'New Arabic'
        verbose_name_plural = 'News Arabic'

    def __str__(self):
        return f"{self.title} | {self.image} | {self.status}"
