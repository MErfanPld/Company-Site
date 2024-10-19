from rest_framework import serializers
from .models import *


class SliderEnglishSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlidersEnglish
        fields = "__all__"


class SliderArabicSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlidersArabic
        fields = "__all__"


class AboutUsEnglishSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsEnglish
        fields = "__all__"



class AboutUsArabicSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsArabic
        fields = "__all__"



class ChooseUsEnglishSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChooseUsEnglish
        fields = "__all__"


class ChooseUsArabicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChooseUsArabic
        fields = "__all__"


class ServiceEnglishSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceEnglish
        fields = "__all__"


class ServiceArabicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceArabic
        fields = "__all__"


class CommentsEnglishSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentsEnglish
        fields = "__all__"


class CommentsArabicSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentsArabic
        fields = "__all__"


class SuggestionsEnglishSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuggestionsEnglish
        fields = "__all__"


class SuggestionsArabicSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuggestionsArabic
        fields = "__all__"



class FAQEnglishSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQEnglish
        fields = "__all__"


class FAQArabicSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQArabic
        fields = "__all__"
