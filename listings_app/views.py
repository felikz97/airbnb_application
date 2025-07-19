from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Property
from .serializers import PropertySerializer
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['location', 'price_per_night']
    search_fields = ['title', 'description']

    @method_decorator(cache_page(60 * 5))  # 5 minutes
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(host=self.request.user)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.host != request.user:
            return Response({'detail': 'Unauthorized.'}, status=403)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.host != request.user:
            return Response({'detail': 'Unauthorized.'}, status=403)
        return super().destroy(request, *args, **kwargs)
    