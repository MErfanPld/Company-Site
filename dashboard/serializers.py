from rest_framework import serializers
from home.models import *


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sliders
        fields = "__all__"


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = "__all__"



class ChooseUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChooseUs
        fields = "__all__"



class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"



class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"



class SuggestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestions
        fields = "__all__"



# class FAQEnglishSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = FAQ
#         exclude = ["question_ar", "answer_ar"]

