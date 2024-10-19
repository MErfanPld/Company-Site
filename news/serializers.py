from rest_framework import serializers
from .models import *



class NewsEnglishSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsEnglish
        fields = "__all__"


class NewsArabicSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsArabic
        fields = "__all__"