from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PaymentViewSet

router = DefaultRouter()
router.register(r'payments', PaymentViewSet, basename='payment')

urlpatterns = [
    path('', include(router.urls)),
]
# This file defines the URL routing for the payments_app, including the PaymentViewSet.
# It uses Django REST Framework's DefaultRouter to automatically generate routes for the PaymentViewSet.