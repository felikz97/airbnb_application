from django.db import models
from bookings_app.models import Booking

class Payment(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name='payment')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    method = models.CharField(
        max_length=50,
        choices=[('card', 'Card'), ('paypal', 'PayPal')]
    )
    status = models.CharField(
        max_length=20,
        choices=[('success', 'Success'), ('failed', 'Failed'), ('pending', 'Pending')],
        default='pending'
    )
    def __str__(self):
        return f'Payment for Booking {self.booking.id} - {self.status}'