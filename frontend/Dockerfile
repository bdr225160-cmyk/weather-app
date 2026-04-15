# نستخدم Nginx لخدمة الصفحة الأمامية
FROM nginx:alpine

# نسخ صفحة الويب
COPY index.html /usr/share/nginx/html/index.html

# نسخ إعدادات Nginx (للـ proxy للـ backend)
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
