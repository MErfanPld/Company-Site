from rest_framework import serializers
from .models import *



class ProductEnglishSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductEnglish
        fields = "__all__"


class ProductArabicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductArabic
        fields = "__all__"
