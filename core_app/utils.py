# core_app/utils.py or middleware.py
import requests

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
