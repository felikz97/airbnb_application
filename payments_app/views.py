from rest_framework import viewsets, permissions
from .models import Payment
from .serializers import PaymentSerializer
from core_app.throttles import PaymentThrottle

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]
    throttle_classes = [PaymentThrottle]

    def perform_create(self, serializer):
        # Validate payment logic, prevent double payment
        booking = serializer.validated_data['booking']
        if hasattr(booking, 'payment'):
            raise serializer.ValidationError('Payment already exists for this booking.')
        serializer.save(status='pending')