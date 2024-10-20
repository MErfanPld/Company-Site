from django.shortcuts import render
from rest_framework.generics import *
from .models import *
from .serializers import *

# Create your views here.

# * =================== Product ===================

class ProductEnglishListView(ListAPIView):
    queryset = ProductEnglish.objects.filter(status=True)
    serializer_class = ProductEnglishSerializer


class ProductArabicListView(ListAPIView):
    queryset = ProductArabic.objects.filter(status=True)
    serializer_class = ProductArabicSerializer