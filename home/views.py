from django.shortcuts import render
from rest_framework.generics import *
from .models import *
from .serializers import *

# Create your views here.

# * =================== Slider ===================


class SliderEnglishListView(ListAPIView):
    queryset = Sliders.objects.filter(status=True)
    serializer_class = SliderEnglishSerializer


class SliderArabicListView(ListAPIView):
    queryset = Sliders.objects.filter(status=True)
    serializer_class = SliderArabicSerializer

# * =================== AboutUs ===================


class AboutUsEnglishListView(ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsEnglishSerializer


class AboutUsArabicListView(ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsArabicSerializer

# * =================== ChooseUs ===================


class ChooseUsEnglishListView(ListAPIView):
    queryset = ChooseUs.objects.all()
    serializer_class = ChooseUsEnglishSerializer


class ChooseUsArabicListView(ListAPIView):
    queryset = ChooseUs.objects.all()
    serializer_class = ChooseUsArabicSerializer

# * =================== Service ===================


class ServiceEnglishListView(ListAPIView):
    queryset = Service.objects.filter(status=True)
    serializer_class = ServiceEnglishSerializer


class ServiceArabicListView(ListAPIView):
    queryset = Service.objects.filter(status=True)
    serializer_class = ServiceArabicSerializer

# * =================== Comments ===================


class CommentsEnglishListView(ListAPIView):
    queryset = Comments.objects.filter(status=True)
    serializer_class = CommentsEnglishSerializer


class CommentsArabicListView(ListAPIView):
    queryset = Comments.objects.filter(status=True)
    serializer_class = CommentsArabicSerializer

# * =================== Suggestions ===================


class SuggestionsEnglishListView(ListAPIView):
    queryset = Suggestions.objects.filter(status=True)
    serializer_class = SuggestionsEnglishSerializer


class SuggestionsArabicListView(ListAPIView):
    queryset = Suggestions.objects.filter(status=True)
    serializer_class = SuggestionsArabicSerializer


# * =================== FAQ ===================


class FAQEnglishListView(ListAPIView):
    queryset = FAQ.objects.filter(status=True)
    serializer_class = FAQEnglishSerializer


class FAQArabicListView(ListAPIView):
    queryset = FAQ.objects.filter(status=True)
    serializer_class = FAQArabicSerializer
