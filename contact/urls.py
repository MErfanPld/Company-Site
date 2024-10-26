from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

app_name = "contacts"

router = DefaultRouter()
router.register(r'contacts', ContactUsViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path("contacts/slider/en/", ContactSliderEnglishListView.as_view(),
         name="contact_slider_english_list"),
    path("contacts/slider/ar/", ContactSliderArabicListView.as_view(),
         name="contact_slider_arabic_list"),
]
