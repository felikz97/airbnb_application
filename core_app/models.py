# core_app/middleware.py
import requests

def get_client_ip(request):
    return request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')

def get_client_location(ip):
    try:
        response = requests.get(f'https://ipapi.co/{ip}/json/')
        if response.status_code == 200:
            data = response.json()
            return {
                "ip": ip,
                "city": data.get("city"),
                "region": data.get("region"),
                "country": data.get("country_name"),
                "latitude": data.get("latitude"),
                "longitude": data.get("longitude"),
                "org": data.get("org"),
            }
    except Exception as e:
        print("GeoIP Error:", e)
    return {"ip": ip, "error": "location not found"}

class LogUserRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = get_client_ip(request)
        location = get_client_location(ip)
        print(f"[REQUEST] {request.method} {request.path} from {location}")
        return self.get_response(request)
# core_app/middleware.py