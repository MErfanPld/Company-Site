import aboutus.utils
from rest_framework import serializers
from home.models import *
from news.models import *
from aboutus.models import *
from products.models import ProductArabic, ProductEnglish


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


class NewsEnglishSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsEnglish
        fields = "__all__"


class NewsArabicSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsArabic
        fields = "__all__"


class ProductEnglishSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductEnglish
        fields = "__all__"


class ProductArabicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductArabic
        fields = "__all__"


class AboutSlidersEnglishSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutSlidersEnglish
        fields = "__all__"


class AboutSlidersArabicSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutSlidersArabic
        fields = "__all__"


class AchievementEnglishSerializer(serializers.ModelSerializer):
    class Meta:
        model = AchievementEnglish
        fields = "__all__"


class AchievementArabicSerializer(serializers.ModelSerializer):
    class Meta:
        model = AchievementArabic
        fields = "__all__"

class TeamEnglishSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamEnglish
        fields = "__all__"


class TeamArabicSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamArabic
        fields = "__all__"
