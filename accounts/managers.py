from django.contrib.auth.base_user import BaseUserManager

from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def normalize_phoneNumber(self, phoneNumber):
        # اینجا می‌توانید کدهایی برای نرمال‌سازی شماره تلفن اضافه کنید
        # برای مثال حذف فضاها، پر کردن شماره تلفن با پیش‌شماره و غیره
        return phoneNumber.strip()  # به عنوان نمونه فقط فضای اضافی را حذف می‌کند

    def _create_user(self, phoneNumber , username , password, **extra_fields):
        if not phoneNumber:
            raise ValueError('The given phoneNumber must be set')
        if not username:
            raise ValueError('The given username must be set')

        phoneNumber = self.normalize_phoneNumber(phoneNumber)  # استفاده از متد نرمال‌سازی
        user = self.model(phoneNumber=phoneNumber , username=username , **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phoneNumber , username , password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phoneNumber , username , password, **extra_fields)

    def create_superuser(self, phoneNumber , username , password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phoneNumber ,username , password, **extra_fields)

    use_in_migrations = True

    def _create_user(self, phoneNumber , username , password, **extra_fields):
        if not phoneNumber:
            raise ValueError('The given phoneNumber must be set')
        if not username:
            raise ValueError('The given username must be set')

        phoneNumber = self.normalize_phoneNumber(phoneNumber)
        user = self.model(phoneNumber=phoneNumber , username=username , **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phoneNumber , username , password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phoneNumber , username , password, **extra_fields)

    def create_superuser(self, phoneNumber , username , password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phoneNumber ,username , password, **extra_fields)