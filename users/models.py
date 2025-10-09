# users/models.py
from django.db import models

class UserProfile(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    google_id = models.CharField(max_length=255, unique=True)
    profile_picture = models.URLField(max_length=1024, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email