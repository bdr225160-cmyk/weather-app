# 🌤️ Weather App — Docker + Kubernetes

تطبيق ويب لعرض بيانات الطقس باستخدام Docker و Kubernetes.

## 🏗️ معمارية المشروع

```
3 Containers:
├── 🌐 Frontend  — Nginx (يخدم صفحة HTML)
├── 🐍 Backend   — Python Flask (API الطقس)
└── 🔴 Redis     — Cache (يحفظ النتائج 10 دقائق)
```

## ⚡ تشغيل المشروع بـ Docker Compose

```bash
# نسخ المشروع
git clone https://github.com/YOUR_USERNAME/weather-app.git
cd weather-app

# تشغيل الـ containers
docker-compose up --build

# افتح المتصفح على
http://localhost:3000
```

## ☸️ تشغيل على Kubernetes

```bash
# تطبيق جميع الملفات
kubectl apply -f k8s/

# تحقق من الـ pods
kubectl get pods

# تحقق من الـ services
kubectl get services
```

## 📁 هيكل الملفات

```
weather-app/
├── backend/
│   ├── app.py           # Flask API
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── index.html       # واجهة المستخدم
│   ├── nginx.conf
│   └── Dockerfile
├── k8s/
│   ├── redis-deployment.yaml
│   ├── backend-deployment.yaml
│   └── frontend-deployment.yaml
├── docker-compose.yml
└── README.md
```

## 🔑 إضافة API Key حقيقي

1. سجّل على [openweathermap.org](https://openweathermap.org) مجاناً
2. في `docker-compose.yml` غيّر:
   ```yaml
   WEATHER_API_KEY=your_real_key
   ```
   إلى مفتاحك الحقيقي.
