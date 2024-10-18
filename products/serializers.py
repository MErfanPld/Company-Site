from rest_framework import serializers
from .models import *



class ProductEnglishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ["title_ar", "price","desc_ar","content_ar"]


class ProductArabicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ["title_en", "price","desc_en","content_en"]
