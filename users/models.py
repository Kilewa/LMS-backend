from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from PIL import Image
from tinymce.models import HTMLField
from django.db.models.signals import post_save
from django.dispatch import receiver



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    user_name = models.CharField(max_length=60, blank=True)
    user_bio = HTMLField(max_length=300,default="No bio")
    profile_photo = models.ImageField(default='default.jpg', upload_to='profile_pics')
    user_email = models.EmailField(max_length=255,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)


    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    @receiver(post_save, sender=User) 
    def save_profile(sender,instance,**kwargs):
        instance.profile.save()  