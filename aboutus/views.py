from django.shortcuts import render
from rest_framework.generics import *
from .models import *
from .serializers import *

# Create your views here.

# * =================== Achievement ===================


class AchievementEnglishListView(ListAPIView):
    queryset = AchievementEnglish.objects.filter(status=True)
    serializer_class = AchievementEnglishSerializer


class AchievementArabicListView(ListAPIView):
    queryset = AchievementArabic.objects.filter(status=True)
    serializer_class = AchievementArabicSerializer

# * =================== Team ===================


class TeamEnglishListView(ListAPIView):
    queryset = TeamEnglish.objects.all()
    serializer_class = TeamEnglishSerializer


class TeamArabicListView(ListAPIView):
    queryset = TeamArabic.objects.all()
    serializer_class = TeamArabicSerializer
