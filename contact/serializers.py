from rest_framework import serializers
from .models import *


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ['fullname', 'email', 'phone', 'content']


class ContactSliderEnglishSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSlidersEnglish
        fields = "__all__"


class ContactSliderArabicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSlidersArabic
        fields = "__all__"
