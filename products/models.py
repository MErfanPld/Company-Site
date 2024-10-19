from django.db import models

from .utils import upload_image_product

# Create your models here.


class ProductEnglish(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    desc = models.TextField()
    content = models.TextField(verbose_name="Content EN")
    image = models.ImageField(
        upload_to=upload_image_product, null=True, blank=True, verbose_name='Image')
    status = models.BooleanField(
        default=True, verbose_name='Is Active?')

    class Meta:
        verbose_name = 'Product English'
        verbose_name_plural = 'Products English'

    def __str__(self):
        return f"{self.title} | {self.image} | {self.status}"


class ProductArbic(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    desc = models.TextField()
    content = models.TextField(verbose_name="Content EN")
    image = models.ImageField(
        upload_to=upload_image_product, null=True, blank=True, verbose_name='Image')
    status = models.BooleanField(
        default=True, verbose_name='Is Active?')

    class Meta:
        verbose_name = 'Product Arbic'
        verbose_name_plural = 'Products Arbic'

    def __str__(self):
        return f"{self.title} | {self.image} | {self.status}"
