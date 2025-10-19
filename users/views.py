# users/views.py
from rest_framework import status
from django.contrib.auth.models import User
from .models import UserProfile
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.db import transaction

# GoogleLoginView can remain the same or be updated for consistency
class GoogleLoginView(APIView):
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        name = request.data.get('name')
        if not email:
            return Response({'error': 'Email is required'}, status=400)

        user, _ = User.objects.get_or_create(username=email, defaults={'email': email, 'first_name': name})
        UserProfile.objects.get_or_create(user=user, defaults={'email': email, 'name': name})
        
        refresh = RefreshToken.for_user(user)
        return Response({'refresh': str(refresh), 'access': str(refresh.access_token)})


class PhoneAuthView(APIView):
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        phone_number = request.data.get('phone_number')
        if not phone_number:
            return Response({'error': 'Phone number is required'}, status=400)

        # First, check if a profile with this phone number exists
        profile = UserProfile.objects.filter(phone_number=phone_number).first()
        
        if profile:
            # If the profile exists, the user is not new.
            is_new_user = False
            user = profile.user
        else:
            # If the profile does not exist, the user is new.
            is_new_user = True
            # Create the Django User first, ensuring the username is unique.
            user = User.objects.create_user(username=phone_number)
            # Now create the UserProfile and link it to the new User.
            profile = UserProfile.objects.create(
                user=user,
                phone_number=phone_number,
                email=f"{user.username}@temp.cafco.com", # Unique temporary email
                name="New User"
            )
            
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'is_new_user': is_new_user,
            'user': {
                'name': profile.name,
                'email': profile.email
            }
        })

class UpdateUserProfileView(APIView):
    def post(self, request, *args, **kwargs):
        phone_number = request.data.get('phone_number')
        name = request.data.get('name')
        email = request.data.get('email')

        if not all([phone_number, name, email]):
            return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            profile = UserProfile.objects.get(phone_number=phone_number)
            profile.name = name
            profile.email = email
            profile.user.first_name = name
            profile.user.email = email
            profile.save()
            profile.user.save()
            return Response({'success': 'Profile updated successfully'}, status=status.HTTP_200_OK)
        except UserProfile.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)