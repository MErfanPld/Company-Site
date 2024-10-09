from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactUsViewSet

app_name = "contacts"

router = DefaultRouter()
router.register(r'contacts', ContactUsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]