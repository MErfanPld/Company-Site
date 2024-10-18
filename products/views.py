from django.shortcuts import render
from rest_framework.generics import *
from .models import *
from .serializers import *

# Create your views here.

# * =================== Product ===================

class ProductEnglishListView(ListAPIView):
    queryset = Product.objects.filter(status=True)
    serializer_class = ProductEnglishSerializer


class ProductArabicListView(ListAPIView):
    queryset = Product.objects.filter(status=True)
    serializer_class = ProductArabicSerializer