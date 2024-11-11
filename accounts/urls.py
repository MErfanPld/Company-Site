from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView,TokenObtainPairView

from . import views

app_name = "accounts"

urlpatterns = [
    path("accounts/register/", views.UserRegisterationAPIView.as_view(), name="create-user"),
    path("accounts/login/", views.UserLoginAPIView.as_view(), name="login-user"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("accounts/logout/", views.UserLogoutAPIView.as_view(), name="logout-user"),
]