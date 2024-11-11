from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("email_verified_at", "date_joined", "last_login",
                   "is_superuser", "is_active", "is_staff", "level",)


class UserRegisterationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "phoneNumber", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)



class UserLoginSerializer(serializers.Serializer):
    phoneNumber = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        phoneNumber = data.get('phoneNumber')
        password = data.get('password')

        user = authenticate(username=phoneNumber, password=password)
        
        if user is None:
            raise serializers.ValidationError("Incorrect Credentials")
        
        return user