from django.urls import path, include
from . import views

app_name = "state"

urlpatterns = [
    path("sliders/en/", views.SliderEnglishListView.as_view(), name="slider_english_list"),
    path("sliders/ar/", views.SliderArabicListView.as_view(), name="slider_arabic_list"),
    
    path("about/en/", views.AboutUsEnglishListView.as_view(), name="about_english_list"),
    path("about/ar/", views.AboutUsArabicListView.as_view(), name="about_arabic_list"),
    
    path("choose_us/en/", views.ChooseUsEnglishListView.as_view(), name="choose_us_english_list"),
    path("choose_us/ar/", views.ChooseUsArabicListView.as_view(), name="choose_us_arabic_list"),

    path("service/en/", views.ServiceEnglishListView.as_view(), name="service_english_list"),
    path("service/ar/", views.ServiceArabicListView.as_view(), name="service_arabic_list"),
    
    path("comments/en/", views.CommentsEnglishListView.as_view(), name="comments_english_list"),
    path("comments/ar/", views.CommentsArabicListView.as_view(), name="comments_arabic_list"),
    
    path("suggestions/en/", views.SuggestionsEnglishListView.as_view(), name="suggestions_english_list"),
    path("suggestions/ar/", views.SuggestionsArabicListView.as_view(), name="suggestions_arabic_list"),

    path("faq/en/", views.FAQEnglishListView.as_view(), name="faq_english_list"),
    path("faq/ar/", views.FAQArabicListView.as_view(), name="faq_arabic_list"),
]