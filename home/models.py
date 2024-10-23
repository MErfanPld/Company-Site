from django.db import models
from .utils import *

# Create your models here.


class SlidersEnglish(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    sub_title = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Sub Title")
    image = models.ImageField(
        upload_to=upload_image_sliders, null=True, blank=True, verbose_name='Image')
    status = models.BooleanField(
        default=True, verbose_name='Is Active?')

    class Meta:
        verbose_name = 'Slider English'
        verbose_name_plural = 'Sliders English'

    def __str__(self):
        return f"{self.title} | {self.image} | {self.status}"


class SlidersArabic(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    sub_title = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Sub Title")
    image = models.ImageField(
        upload_to=upload_image_sliders, null=True, blank=True, verbose_name='Image')
    status = models.BooleanField(
        default=True, verbose_name='Is Active?')

    class Meta:
        verbose_name = 'Slider Arabic'
        verbose_name_plural = 'Sliders Arabic'

    def __str__(self):
        return f"{self.title}  | {self.image} | {self.status}"


class AboutUsEnglish(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    content = models.TextField(verbose_name="Content")
    count_employee = models.IntegerField(verbose_name="Number of employees")
    count_product = models.IntegerField(verbose_name="Number of products")
    image = models.ImageField(
        upload_to=upload_image_about, null=True, blank=True, verbose_name='Image')

    class Meta:
        verbose_name = 'AboutUs English'
        verbose_name_plural = 'AboutUs English'

    def __str__(self):
        return f"{self.title}  | {self.image}"


class AboutUsArabic(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    content = models.TextField(verbose_name="Content")
    count_employee = models.IntegerField(verbose_name="Number of employees")
    count_product = models.IntegerField(verbose_name="Number of products")
    image = models.ImageField(
        upload_to=upload_image_about, null=True, blank=True, verbose_name='Image')

    class Meta:
        verbose_name = 'AboutUs Arabic'
        verbose_name_plural = 'AboutUs Arabic'

    def __str__(self):
        return f"{self.title} | {self.image}"


class ChooseUsEnglish(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title EN")
    content = models.TextField(verbose_name="Content EN")
    image = models.ImageField(
        upload_to=upload_image_choose_us, null=True, blank=True, verbose_name='Image')

    class Meta:
        verbose_name = 'ChooseUs English'
        verbose_name_plural = 'ChooseUs English'

    def __str__(self):
        return f"{self.title} | {self.image}"


class ChooseUsArabic(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title EN")
    content = models.TextField(verbose_name="Content EN")
    image = models.ImageField(
        upload_to=upload_image_choose_us, null=True, blank=True, verbose_name='Image')

    class Meta:
        verbose_name = 'ChooseUs Arabic'
        verbose_name_plural = 'ChooseUs Arabic'

    def __str__(self):
        return f"{self.title} | {self.image}"


class ServiceEnglish(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title EN")
    content = models.TextField(verbose_name="Content EN")
    image = models.ImageField(
        upload_to=upload_image_service, null=True, blank=True, verbose_name='Image')
    icon_img = models.ImageField(
        upload_to=upload_image_service_icon, null=True, blank=True, verbose_name='Image Icon')
    status = models.BooleanField(
        default=True, verbose_name='Is Active?')

    class Meta:
        verbose_name = 'Service English'
        verbose_name_plural = 'Service English'

    def __str__(self):
        return f"{self.title} | {self.image} | {self.status}"


class ServiceArabic(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title EN")
    content = models.TextField(verbose_name="Content EN")
    image = models.ImageField(
        upload_to=upload_image_service, null=True, blank=True, verbose_name='Image')
    icon_img = models.ImageField(
        upload_to=upload_image_service_icon, null=True, blank=True, verbose_name='Image Icon')
    status = models.BooleanField(
        default=True, verbose_name='Is Active?')

    class Meta:
        verbose_name = 'Service Arabic'
        verbose_name_plural = 'Service Arabic'

    def __str__(self):
        return f"{self.title} | {self.image} | {self.status}"


class CommentsEnglish(models.Model):
    image = models.ImageField(
        upload_to=upload_image_comment, null=True, blank=True, verbose_name='Image')
    content = models.TextField(verbose_name="Content EN")
    fullname = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Full Name EN")
    country = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Country EN")
    status = models.BooleanField(
        default=True, verbose_name='Is Active?')

    class Meta:
        verbose_name = 'Comments English'
        verbose_name_plural = 'Comments English'

    def __str__(self):
        return f"{self.fullname} | {self.image} | {self.status}"

class CommentsArabic(models.Model):
    image = models.ImageField(
        upload_to=upload_image_comment, null=True, blank=True, verbose_name='Image')
    content = models.TextField(verbose_name="Content EN")
    fullname = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Full Name EN")
    country = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Country EN")
    status = models.BooleanField(
        default=True, verbose_name='Is Active?')

    class Meta:
        verbose_name = 'Comments Arabic'
        verbose_name_plural = 'Comments Arabic'

    def __str__(self):
        return f"{self.fullname} | {self.image} | {self.status}"


class SuggestionsEnglish(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title EN")
    content = models.TextField(verbose_name="Content EN")
    icon_img = models.ImageField(
        upload_to=upload_image_suggestions_icon, null=True, blank=True, verbose_name='Image Icon')
    status = models.BooleanField(
        default=True, verbose_name='Is Active?')

    class Meta:
        verbose_name = 'Suggestions English'
        verbose_name_plural = 'Suggestions English'

    def __str__(self):
        return f"{self.title} |{self.status}"

class SuggestionsArabic(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title EN")
    content = models.TextField(verbose_name="Content EN")
    icon_img = models.ImageField(
        upload_to=upload_image_suggestions_icon, null=True, blank=True, verbose_name='Image Icon')
    status = models.BooleanField(
        default=True, verbose_name='Is Active?')

    class Meta:
        verbose_name = 'Suggestions Arabic'
        verbose_name_plural = 'Suggestions Arabic'

    def __str__(self):
        return f"{self.title} |{self.status}"


class FAQEnglish(models.Model):
    question = models.CharField(max_length=255, verbose_name="Question EN")
    answer = models.TextField(verbose_name="Answer EN")
    status = models.BooleanField(default=True, verbose_name="Is Active?")

    class Meta:
        verbose_name = "FAQ English"
        verbose_name_plural = "FAQs English"

    def __str__(self):
        return f"{self.question} |{self.status} "

class FAQArabic(models.Model):
    question = models.CharField(max_length=255, verbose_name="Question EN")
    answer = models.TextField(verbose_name="Answer EN")
    status = models.BooleanField(default=True, verbose_name="Is Active?")

    class Meta:
        verbose_name = "FAQ Arabic"
        verbose_name_plural = "FAQs Arabic"

    def __str__(self):
        return f"{self.question} |{self.status} "