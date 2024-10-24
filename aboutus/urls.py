from django.urls import path, include
from . import views

app_name = "about-us"

urlpatterns = [
    path("about-us/achievement/en/", views.AchievementEnglishListView.as_view(),
         name="achievement_english_list"),
    path("about-us/achievement/ar/", views.AchievementArabicListView.as_view(),
         name="achievement_arabic_list"),

    path("about-us/team/en/", views.TeamEnglishListView.as_view(),
         name="team_english_list"),
    path("about-us/team/ar/", views.TeamArabicListView.as_view(),
         name="team_arabic_list"),

]
