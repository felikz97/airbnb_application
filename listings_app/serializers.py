from rest_framework import serializers
from .models import Property, PropertyImage
from users_app.models import User
from rest_framework import serializers


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'
        read_only_fields = ['id', 'host', 'created_at']

    def validate_price_per_night(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than 0.")
        return value

    def validate_max_guests(self, value):
        if value < 1:
            raise serializers.ValidationError("There must be at least 1 guest allowed.")
        return value 
