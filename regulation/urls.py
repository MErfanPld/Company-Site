from django.urls import path, include
from . import views

app_name = "settings"

urlpatterns = [
    path("settings/en/", views.SettingsEnglishListView.as_view(), name="en_setting_list"),
    path("settings/ar/", views.SettingsArabicListView.as_view(), name="ar_setting_list"),
    path("social/", views.SocialListView.as_view(), name="social_list"),
]