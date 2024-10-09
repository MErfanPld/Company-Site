from django.db import models
from .utils import *

# Create your models here.


class Sliders(models.Model):
    title_en = models.CharField(max_length=255, verbose_name="Title EN")
    title_ar = models.CharField(max_length=255, verbose_name="Title AR")
    sub_title_en = models.CharField(
        max_length=255, null=True, blank=True,verbose_name="Sub Title EN")
    sub_title_ar = models.CharField(
        max_length=255, null=True, blank=True,verbose_name="Sub Title AR")
    image = models.ImageField(
        upload_to=upload_image_sliders, null=True, blank=True, verbose_name='Image')
    status = models.BooleanField(
        default=True, verbose_name='Is Active?')

    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Sliders'

    def __str__(self):
        return f"{self.title_en} | {self.title_ar} | {self.image} | {self.status}"


class AboutUs(models.Model):
    title_en = models.CharField(max_length=255, verbose_name="Title EN")
    title_ar = models.CharField(max_length=255, verbose_name="Title AR")
    content_en = models.TextField(verbose_name="Content EN")
    content_ar = models.TextField(verbose_name="Content AR")
    count_employee = models.IntegerField(verbose_name="Number of employees")
    count_product = models.IntegerField(verbose_name="Number of products")
    image = models.ImageField(
        upload_to=upload_image_about, null=True, blank=True, verbose_name='Image')

    class Meta:
        verbose_name = 'AboutUs'
        verbose_name_plural = 'AboutUs'

    def __str__(self):
        return f"{self.title_en} | {self.title_ar} | {self.image}"


class ChooseUs(models.Model):
    title_en = models.CharField(max_length=255, verbose_name="Title EN")
    title_ar = models.CharField(max_length=255, verbose_name="Title AR")
    content_en = models.TextField(verbose_name="Content EN")
    content_ar = models.TextField(verbose_name="Content AR")
    image = models.ImageField(
        upload_to=upload_image_choose_us, null=True, blank=True, verbose_name='Image')

    class Meta:
        verbose_name = 'ChooseUs'
        verbose_name_plural = 'ChooseUs'

    def __str__(self):
        return f"{self.title_en} | {self.title_ar} | {self.image}"


class Service(models.Model):
    title_en = models.CharField(max_length=255, verbose_name="Title EN")
    title_ar = models.CharField(max_length=255, verbose_name="Title AR")
    content_en = models.TextField(verbose_name="Content EN")
    content_ar = models.TextField(verbose_name="Content AR")
    image = models.ImageField(
        upload_to=upload_image_service, null=True, blank=True, verbose_name='Image')
    icon_img = models.ImageField(
        upload_to=upload_image_service_icon, null=True, blank=True, verbose_name='Image Icon')
    status = models.BooleanField(
        default=True, verbose_name='Is Active?')

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Service'

    def __str__(self):
        return f"{self.title_en} | {self.title_ar} | {self.image} | {self.status}"


class Comments(models.Model):
    image = models.ImageField(
        upload_to=upload_image_comment, null=True, blank=True, verbose_name='Image')
    content_en = models.TextField(verbose_name="Content EN")
    content_ar = models.TextField(verbose_name="Content AR")
    fullname_en = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Full Name EN")
    fullname_ar = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Full Name AR")
    status = models.BooleanField(
        default=True, verbose_name='Is Active?')

    class Meta:
        verbose_name = 'Comments'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f"{self.fullname_en} | {self.image} | {self.status}"


class Suggestions(models.Model):
    title_en = models.CharField(max_length=255, verbose_name="Title EN")
    title_ar = models.CharField(max_length=255, verbose_name="Title AR")
    content_en = models.TextField(verbose_name="Content EN")
    content_ar = models.TextField(verbose_name="Content AR")
    icon_img = models.ImageField(
        upload_to=upload_image_suggestions_icon, null=True, blank=True, verbose_name='Image Icon')
    status = models.BooleanField(
        default=True, verbose_name='Is Active?')

    class Meta:
        verbose_name = 'Suggestions'
        verbose_name_plural = 'Suggestions'

    def __str__(self):
        return f"{self.title_en} | {self.title_ar} | {self.status}"


class FAQ(models.Model):
    question_en = models.CharField(max_length=255, verbose_name="Question EN")
    question_ar = models.CharField(max_length=255, verbose_name="Question AR")
    answer_en = models.TextField(verbose_name="Answer EN")
    answer_ar = models.TextField(verbose_name="Answer AR")
    status = models.BooleanField(default=True, verbose_name="Is Active?")
    
    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    def __str__(self):
        return f"{self.question_en} | {self.question_ar}"
