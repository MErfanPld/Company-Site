from rest_framework import serializers
from .models import *

class AboutSliderEnglishSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutSlidersEnglish
        fields = "__all__"


class AboutSliderArabicSerializer(serializers.ModelSerializer):
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
