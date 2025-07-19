import logging
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Booking
from .serializers import BookingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

logger = logging.getLogger('bookings')

class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            logger.info("Admin user %s accessed all bookings.", user.username)
            return Booking.objects.all()
        logger.debug("User %s accessed their bookings.", user.username)
        return Booking.objects.filter(guest=user)

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(guest=self.request.user)
        else:
            raise PermissionDenied("You must be logged in to create a booking.")

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.guest != request.user and not request.user.is_staff:
            logger.warning("Unauthorized delete attempt by user %s on booking %s", request.user.username, instance.id)
            return Response({'detail': 'Unauthorized.'}, status=status.HTTP_403_FORBIDDEN)
        logger.info("Booking %s deleted by user %s", instance.id, request.user.username)
        return super().destroy(request, *args, **kwargs)
