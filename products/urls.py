from django.urls import path, include
from . import views

app_name = "product"

urlpatterns = [
    path("product/en/", views.ProductEnglishListView.as_view(), name="product_english_list"),
    path("product/ar/", views.ProductArabicListView.as_view(), name="product_arabic_list"),
]