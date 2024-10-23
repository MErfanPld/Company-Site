from django.shortcuts import render
from rest_framework.generics import *
from .models import *
from .serializers import *

# Create your views here.


class SettingsEnglishListView(ListAPIView):
    queryset = SettingsArabic.objects.all()
    serializer_class = SettingsEnglishSerializer


class SettingsArabicListView(ListAPIView):
    queryset = SettingsArabic.objects.all()
    serializer_class = SettingsArabicSerializer


class SocialListView(ListAPIView):
    queryset = Social.objects.all()
    serializer_class = SocialSerializer
