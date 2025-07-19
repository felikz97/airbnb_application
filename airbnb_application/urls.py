"""
URL configuration for airbnb_clone_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.throttling import ScopedRateThrottle
from rest_framework.decorators import throttle_classes
from core_app.throttles import LoginThrottle

schema_view = get_schema_view(
    openapi.Info(
        title="AirBnB Clone API",
        default_version='v1',
        description="Backend endpoints for booking, listings, payments, and reviews.",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)



urlpatterns = [
    path('admin/', admin.site.urls),
    
    
    # App endpoints
    path('api/', include('users_app.urls')),
    path('api/', include('listings_app.urls')),
    path('api/', include('bookings_app.urls')),
    path('api/', include('payments_app.urls')),
    path('api/', include('reviews_app.urls')),
    
    # Auth
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
# This file defines the URL routing for the airbnb_clone_backend project, including admin and API endpoints.
@throttle_classes([LoginThrottle])
class ThrottledLoginView(TokenObtainPairView):
    pass
urlpatterns += [
    path('api/token/', ThrottledLoginView.as_view(), name='token_obtain_pair'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


