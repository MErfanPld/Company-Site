from django.shortcuts import render
from rest_framework.generics import *
from .models import *
from .serializers import *

# Create your views here.

# * =================== News ===================

class NewsEnglishListView(ListAPIView):
    queryset = News.objects.filter(status=True)
    serializer_class = NewsEnglishSerializer


class NewsArabicListView(ListAPIView):
    queryset = News.objects.filter(status=True)
    serializer_class = NewsArabicSerializer