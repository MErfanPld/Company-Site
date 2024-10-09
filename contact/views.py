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
