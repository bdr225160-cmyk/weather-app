from flask import Flask, jsonify, request
from flask_cors import CORS
import redis
import requests
import json
import os

app = Flask(__name__)
CORS(app)

# الاتصال بـ Redis
redis_client = redis.Redis(
    host=os.getenv('REDIS_HOST', 'redis'),
    port=6379,
    decode_responses=True
)

# مفتاح API للطقس (مجاني من OpenWeatherMap)
API_KEY = os.getenv('WEATHER_API_KEY', 'demo')
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route('/health')
def health():
    return jsonify({"status": "ok", "service": "weather-backend"})

@app.route('/api/weather/<city>')
def get_weather(city):
    # نتحقق أول هل البيانات موجودة في Redis (الكاش)
    cache_key = f"weather:{city.lower()}"
    cached = redis_client.get(cache_key)

    if cached:
        data = json.loads(cached)
        data['from_cache'] = True
        return jsonify(data)

    # إذا مو في الكاش، نجيب من API
    if API_KEY == 'demo':
        # بيانات تجريبية للتوضيح
        weather_data = {
            "city": city,
            "temperature": 32,
            "feels_like": 35,
            "description": "مشمس وحار",
            "humidity": 45,
            "wind_speed": 12,
            "icon": "01d",
            "from_cache": False,
            "note": "بيانات تجريبية - أضف API Key حقيقي من openweathermap.org"
        }
    else:
        try:
            response = requests.get(WEATHER_URL, params={
                'q': city,
                'appid': API_KEY,
                'units': 'metric',
                'lang': 'ar'
            })
            if response.status_code != 200:
                return jsonify({"error": "المدينة غير موجودة"}), 404

            raw = response.json()
            weather_data = {
                "city": raw['name'],
                "temperature": round(raw['main']['temp']),
                "feels_like": round(raw['main']['feels_like']),
                "description": raw['weather'][0]['description'],
                "humidity": raw['main']['humidity'],
                "wind_speed": raw['wind']['speed'],
                "icon": raw['weather'][0]['icon'],
                "from_cache": False
            }
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    # نحفظ في Redis لمدة 10 دقائق
    redis_client.setex(cache_key, 600, json.dumps(weather_data))
    return jsonify(weather_data)

@app.route('/api/cities')
def popular_cities():
    cities = ["Riyadh", "Jeddah", "Mecca", "Dubai", "Cairo", "London", "Tokyo", "New York"]
    return jsonify({"cities": cities})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
