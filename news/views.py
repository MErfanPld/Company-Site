from django.shortcuts import render
from rest_framework.generics import *
from .models import *
from .serializers import *

# Create your views here.

# * =================== News ===================

class NewsEnglishListView(ListAPIView):
    queryset = NewsEnglish.objects.filter(status=True)
    serializer_class = NewsEnglishSerializer


class NewsArabicListView(ListAPIView):
    queryset = NewsArabic.objects.filter(status=True)
    serializer_class = NewsArabicSerializer