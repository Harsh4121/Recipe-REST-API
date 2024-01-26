# models.py
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add any additional fields you need for the user profile

class Receipe(models.Model):
    receipe_image = models.ImageField(upload_to='receipe_images/')
    receipe_name = models.CharField(max_length=255)
    receipe_discription = models.TextField()

# Add any other models you need
