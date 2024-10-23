from rest_framework import serializers
from .models import *


class SettingsEnglishSerializer(serializers.ModelSerializer):
    class Meta:
        model = SettingsEnglish
        fields = "__all__"

class SettingsArabicSerializer(serializers.ModelSerializer):
    class Meta:
        model = SettingsArabic
        fields = "__all__"


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = "__all__"
