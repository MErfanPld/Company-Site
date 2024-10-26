from django.db import models

from contact.utils import upload_image_contact_sliders

# Create your models here.


class ContactUs(models.Model):
    fullname = models.CharField(max_length=255, verbose_name="Full Name")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=11, verbose_name="Phone")
    content = models.TextField(verbose_name="Content")
    status = models.BooleanField(default=False, verbose_name="Is Read?")
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date Submit"
    )

    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us'

    def __str__(self):
        return f"{self.fullname} | {self.email} | {self.phone}"



class ContactSlidersEnglish(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    sub_title = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Sub Title")
    image = models.ImageField(
        upload_to=upload_image_contact_sliders, null=True, blank=True, verbose_name='Image')
    status = models.BooleanField(
        default=True, verbose_name='Is Active?')

    class Meta:
        verbose_name = 'Contact Slider English'
        verbose_name_plural = 'Contact Sliders English'

    def __str__(self):
        return f"{self.title} | {self.image} | {self.status}"


class ContactSlidersArabic(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    sub_title = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Sub Title")
    image = models.ImageField(
        upload_to=upload_image_contact_sliders, null=True, blank=True, verbose_name='Image')
    status = models.BooleanField(
        default=True, verbose_name='Is Active?')

    class Meta:
        verbose_name = 'Contact Slider Arabic'
        verbose_name_plural = 'Contact Sliders Arabic'

    def __str__(self):
        return f"{self.title}  | {self.image} | {self.status}"


