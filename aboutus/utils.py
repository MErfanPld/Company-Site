import time
from django.urls import reverse
from django.utils.text import slugify


def upload_image_achievement(instance, filename):
    path = 'uploads/' + 'achievement/' + \
        slugify(instance.title, allow_unicode=True)
    name = str(time.time()) + '-' + str(instance.title) + '-' + filename
    return path + '/' + name

def upload_image_team(instance, filename):
    path = 'uploads/' + 'team/' + \
        slugify(instance.fullname, allow_unicode=True)
    name = str(time.time()) + '-' + str(instance.fullname) + '-' + filename
    return path + '/' + name