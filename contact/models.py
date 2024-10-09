from django.db import models

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
