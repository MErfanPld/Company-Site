import time
from django.urls import reverse
from django.utils.text import slugify


def upload_image_news(instance, filename):
    path = 'uploads/' + 'news/' + \
        slugify(instance.title_en, allow_unicode=True)
    name = str(time.time()) + '-' + str(instance.title_en) + '-' + filename
    return path + '/' + name
