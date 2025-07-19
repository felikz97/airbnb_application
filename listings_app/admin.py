from django.contrib import admin

# Register your models here.
from .models import Property

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('id', 'host', 'title', 'price_per_night', 'location', 'max_guests', 'created_at')
    search_fields = ('title', 'location')
    list_filter = ('host', 'location')
    ordering = ('-created_at',)
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('host')
    