from rest_framework import serializers
from .models import *



class NewsEnglishSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        exclude = ["title_ar", "content_ar"]


class NewsArabicSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        exclude = ["title_en", "content_en"]