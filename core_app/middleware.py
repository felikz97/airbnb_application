import logging
import requests
from django.utils.timezone import now
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger('django')

class LogRequestMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ip = self.get_client_ip(request)
        user = request.user.username if request.user.is_authenticated else 'Anonymous'
        timestamp = now().strftime('%Y-%m-%d %H:%M:%S')
        location = self.get_location(ip)

        logger.info(f"[{timestamp}] {user} - {ip} - {location} - {request.method} {request.path}")

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0]
        return request.META.get('REMOTE_ADDR', '')

    def get_location(self, ip):
        try:
            res = requests.get(f'https://ipapi.co/{ip}/json/', timeout=2)
            data = res.json()
            return f"{data.get('city', 'Unknown')}, {data.get('country_name', 'Unknown')}"
        except Exception:
            return "Unknown Location"
