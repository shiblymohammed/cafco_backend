# cafco_backend/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Add the URLs for your apps under the /api/ prefix
    path('api/', include('products.urls')),
    path('api/', include('orders.urls')),
    path('api/', include('users.urls')),
]