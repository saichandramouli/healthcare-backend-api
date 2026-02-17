from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),   # 👈 This line is important
    path('api/', include('healthcare.urls')),
]
