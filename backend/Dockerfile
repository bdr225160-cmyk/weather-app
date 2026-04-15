# نستخدم Python خفيف الحجم
FROM python:3.11-slim

# نحدد مجلد العمل داخل الكونتينر
WORKDIR /app

# نسخ ملف المتطلبات أولاً (لتسريع الـ build)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# نسخ باقي الكود
COPY . .

# المنفذ اللي يستمع عليه التطبيق
EXPOSE 5000

# أمر التشغيل
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:app"]
