from django.db import models

from news.utils import upload_image_news

# Create your models here.

class News(models.Model):
    title_en = models.CharField(max_length=255)
    title_ar = models.CharField(max_length=255)
    content_en = models.TextField(verbose_name="Content EN")
    content_ar = models.TextField(verbose_name="Content AR")
    image = models.ImageField(
        upload_to=upload_image_news, null=True, blank=True, verbose_name='Image')
    status = models.BooleanField(
        default=True, verbose_name='Is Active?')

    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'

    def __str__(self):
        return f"{self.title_en} | {self.title_ar} | {self.image} | {self.status}"