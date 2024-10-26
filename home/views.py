from django.shortcuts import render
from rest_framework.generics import *
from .models import *
from .serializers import *

# Create your views here.

# * =================== Slider ===================


class SliderEnglishListView(ListAPIView):
    queryset = SlidersEnglish.objects.filter(status=True)
    serializer_class = SliderEnglishSerializer


class SliderArabicListView(ListAPIView):
    queryset = SlidersArabic.objects.filter(status=True)
    serializer_class = SliderArabicSerializer

# * =================== AboutUs ===================


class AboutUsEnglishListView(ListAPIView):
    queryset = AboutUsEnglish.objects.all()
    serializer_class = AboutUsEnglishSerializer


class AboutUsArabicListView(ListAPIView):
    queryset = AboutUsArabic.objects.all()
    serializer_class = AboutUsArabicSerializer

# * =================== ChooseUs ===================


class ChooseUsEnglishListView(ListAPIView):
    queryset = ChooseUsEnglish.objects.all()
    serializer_class = ChooseUsEnglishSerializer


class ChooseUsArabicListView(ListAPIView):
    queryset = ChooseUsArabic.objects.all()
    serializer_class = ChooseUsArabicSerializer

# * =================== Service ===================


class ServiceEnglishListView(ListAPIView):
    queryset = ServiceEnglish.objects.filter(status=True)
    serializer_class = ServiceEnglishSerializer


class ServiceArabicListView(ListAPIView):
    queryset = ServiceArabic.objects.filter(status=True)
    serializer_class = ServiceArabicSerializer

# * =================== Comments ===================


class CommentsEnglishListView(ListAPIView):
    queryset = CommentsEnglish.objects.filter(status=True)
    serializer_class = CommentsEnglishSerializer


class CommentsArabicListView(ListAPIView):
    queryset = CommentsArabic.objects.filter(status=True)
    serializer_class = CommentsArabicSerializer

# * =================== Suggestions ===================


class SuggestionsEnglishListView(ListAPIView):
    queryset = SuggestionsEnglish.objects.filter(status=True)
    serializer_class = SuggestionsEnglishSerializer


class SuggestionsArabicListView(ListAPIView):
    queryset = SuggestionsArabic.objects.filter(status=True)
    serializer_class = SuggestionsArabicSerializer


# * =================== FAQ ===================


class FAQEnglishListView(ListAPIView):
    queryset = FAQEnglish.objects.filter(status=True)
    serializer_class = FAQEnglishSerializer


class FAQArabicListView(ListAPIView):
    queryset = FAQArabic.objects.filter(status=True)
    serializer_class = FAQArabicSerializer

# * =================== Service Slider ===================


class ServiceSliderEnglishListView(ListAPIView):
    queryset = ServiceSlidersEnglish.objects.filter(status=True)
    serializer_class = ServiceSliderEnglishSerializer


class ServiceSliderArabicListView(ListAPIView):
    queryset = ServiceSlidersArabic.objects.filter(status=True)
    serializer_class = ServiceSliderArabicSerializer