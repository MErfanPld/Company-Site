from django.shortcuts import render
from rest_framework.generics import *
from .models import *
from .serializers import *

# Create your views here.


class SettingListView(ListAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingSerializer


class SocialListView(ListAPIView):
    queryset = Social.objects.all()
    serializer_class = SocialSerializer
