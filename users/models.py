from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    user_name = models.CharField(max_length=60, blank=True)
    profile_photo = models.ImageField(default='default.jpg', upload_to='profile_pics')
    user_email = models.EmailField(max_length=255,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)