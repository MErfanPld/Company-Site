import time
from django.urls import reverse
from django.utils.text import slugify


def upload_image_contact_sliders(instance, filename):
    path = 'uploads/' + 'contact/' +'sliders/' + \
        slugify(instance.title, allow_unicode=True)
    name = str(time.time()) + '-' + str(instance.title) + '-' + filename
    return path + '/' + name
