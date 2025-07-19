from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Property(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='properties')
    title = models.CharField(max_length=255)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    max_guests = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    currency = models.CharField(
        max_length=3,
        choices=[('USD', 'USD'), ('EUR', 'EUR'), ('GBP', 'GBP')],
        default='USD'
    )

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='properties/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Image for {self.property.title} uploaded at {self.uploaded_at}"
    