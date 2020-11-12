from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.conf import settings
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True,blank=True)
    user_name = models.CharField(max_length=60, blank=True)
    profile_photo = CloudinaryField('image')
    user_email = models.EmailField(max_length=255,blank=True)