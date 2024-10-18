import time
from django.urls import reverse
from django.utils.text import slugify


def upload_image_product(instance, filename):
    path = 'uploads/' + 'product/' + \
        slugify(instance.title_en, allow_unicode=True)
    name = str(time.time()) + '-' + str(instance.title_en) + '-' + filename
    return path + '/' + name
