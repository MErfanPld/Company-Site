from rest_framework import serializers
from .models import *


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ['fullname', 'email','phone', 'content']
