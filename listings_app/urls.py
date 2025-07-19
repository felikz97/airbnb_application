from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PropertyViewSet

router = DefaultRouter()
router.register(r'properties', PropertyViewSet, basename='property')

urlpatterns = [
    path('', include(router.urls)),
]

# This file defines the URL routing for the listings app in the Airbnb clone backend.
# It uses Django REST Framework's DefaultRouter to automatically generate routes for the PropertyViewSet.