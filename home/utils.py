import time
from django.urls import reverse
from django.utils.text import slugify


def upload_image_sliders(instance, filename):
    path = 'uploads/' + 'sliders/' + \
        slugify(instance.title_en, allow_unicode=True)
    name = str(time.time()) + '-' + str(instance.title_en) + '-' + filename
    return path + '/' + name


def upload_image_about(instance, filename):
    path = 'uploads/' + 'abouts/' + \
        slugify(instance.title_en, allow_unicode=True)
    name = str(time.time()) + '-' + str(instance.title_en) + '-' + filename
    return path + '/' + name


def upload_image_choose_us(instance, filename):
    path = 'uploads/' + 'choose_us/' + \
        slugify(instance.title_en, allow_unicode=True)
    name = str(time.time()) + '-' + str(instance.title_en) + '-' + filename
    return path + '/' + name


def upload_image_service(instance, filename):
    path = 'uploads/' + 'service/' + \
        slugify(instance.title_en, allow_unicode=True)
    name = str(time.time()) + '-' + str(instance.title_en) + '-' + filename
    return path + '/' + name


def upload_image_service_icon(instance, filename):
    path = 'uploads/' + 'service/' + \
        slugify(instance.title_en, allow_unicode=True)
    name = str(time.time()) + '-' + str(instance.title_en) + '-' + filename
    return path + '/' + name


def upload_image_comment(instance, filename):
    path = 'uploads/' + 'comment/' + \
        slugify(instance.fullname, allow_unicode=True)
    name = str(time.time()) + '-' + str(instance.fullname) + '-' + filename
    return path + '/' + name


def upload_image_suggestions_icon(instance, filename):
    path = 'uploads/' + 'suggestions/' + \
        slugify(instance.title_en, allow_unicode=True)
    name = str(time.time()) + '-' + str(instance.title_en) + '-' + filename
    return path + '/' + name
