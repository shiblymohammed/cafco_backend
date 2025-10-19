# cafco_backend/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # API URLs
    path('api/', include('products.urls')),
    path('api/', include('orders.urls')),
    path('api/users/', include('users.urls')), # <-- CORRECTED LINE
]