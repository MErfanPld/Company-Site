from django.urls import path, include
from . import views

app_name = "news"

urlpatterns = [
    path("news/en/", views.NewsEnglishListView.as_view(), name="news_english_list"),
    path("news/ar/", views.NewsArabicListView.as_view(), name="news_arabic_list"),
]