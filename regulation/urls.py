from django.urls import path, include
from . import views

app_name = "settings"

urlpatterns = [
    path("settings/", views.SettingListView.as_view(), name="setting_list"),
    path("social/", views.SocialListView.as_view(), name="social_list"),
]