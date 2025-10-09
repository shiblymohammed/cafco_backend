# users/views.py
from django.contrib.auth.models import User
from .models import UserProfile
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

class GoogleLoginView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        name = request.data.get('name')

        if not email:
            return Response({'error': 'Email is required'}, status=400)

        # Find or create the standard Django User
        user, created = User.objects.get_or_create(username=email, defaults={'email': email, 'first_name': name})
        
        # Find or create your UserProfile
        UserProfile.objects.get_or_create(email=email, defaults={'name': name, 'google_id': 'some_default_or_real_id'})

        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })