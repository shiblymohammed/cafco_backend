# Create new file: users/urls.py
from django.urls import path
from .views import GoogleLoginView, PhoneAuthView, UpdateUserProfileView

urlpatterns = [
    path('google-login/', GoogleLoginView.as_view(), name='google-login'),
    path('phone-auth/', PhoneAuthView.as_view(), name='phone-auth'),
    path('update-profile/', UpdateUserProfileView.as_view(), name='update-profile'),
]

# In your main cafco_backend/urls.py, make sure to include these URLs:
# path('api/', include('users.urls')),