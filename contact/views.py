from django.shortcuts import render
from rest_framework.generics import *
from rest_framework import viewsets, permissions

from .models import *
from .serializers import *

# Create your views here.

# * =================== Contact Us ===================


class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer


# * =================== Slider ===================


class ContactSliderEnglishListView(ListAPIView):
    queryset = ContactSlidersEnglish.objects.filter(status=True)
    serializer_class = ContactSliderEnglishSerializer


class ContactSliderArabicListView(ListAPIView):
    queryset = ContactSlidersArabic.objects.filter(status=True)
    serializer_class = ContactSliderArabicSerializer
