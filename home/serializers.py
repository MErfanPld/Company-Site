from rest_framework import serializers
from .models import *


class SliderEnglishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sliders
        exclude = ["title_ar", "sub_title_ar"]


class SliderArabicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sliders
        exclude = ["title_en", "sub_title_en"]


class AboutUsEnglishSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        exclude = ["title_ar", "content_ar"]


class AboutUsArabicSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        exclude = ["title_en", "content_en"]


class ChooseUsEnglishSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChooseUs
        exclude = ["title_ar", "content_ar"]


class ChooseUsArabicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChooseUs
        exclude = ["title_en", "content_en"]


class ServiceEnglishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        exclude = ["title_ar", "content_ar"]


class ServiceArabicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        exclude = ["title_en", "content_en"]


class CommentsEnglishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        exclude = ["fullname_ar", "content_ar", "country_ar"]


class CommentsArabicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        exclude = ["fullname_en", "content_en", "country_en"]


class SuggestionsEnglishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestions
        exclude = ["title_ar", "content_ar"]


class SuggestionsArabicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestions
        exclude = ["title_en", "content_en"]


class FAQEnglishSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        exclude = ["question_ar", "answer_ar"]


class FAQArabicSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        exclude = ["question_en", "answer_en"]
