# Create new file: users/urls.py
from django.urls import path
from .views import GoogleLoginView

urlpatterns = [
    path('google-login/', GoogleLoginView.as_view(), name='google-login'),
]

# In your main cafco_backend/urls.py, make sure to include these URLs:
# path('api/', include('users.urls')),