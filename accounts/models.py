from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from accounts.managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(('username'), max_length=30, unique=True)
    email = models.EmailField(('email'), unique=True)
    first_name = models.CharField(('first name'), max_length=30, blank=True)
    last_name = models.CharField(('last name'), max_length=30, blank=True)
    phoneNumber = models.CharField(('phone number'), max_length=11, blank=True, unique=True)  # اضافه کردن unique=True
    date_joined = models.DateTimeField(('date joined'), default=timezone.now)
    last_login = models.DateTimeField(('last login'), auto_now=True)
    is_superuser = models.BooleanField(('is superuser'), default=False)
    is_active = models.BooleanField(('active'), default=True)
    is_staff = models.BooleanField(('is staff'), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phoneNumber'  # استفاده از phoneNumber به عنوان فیلد نام کاربری
    REQUIRED_FIELDS = ['username', 'password']

    def __str__(self):
        return f'{self.username}, {self.phoneNumber}'

