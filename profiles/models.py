from django.db import models
from authentication.models import Users
from django.core.exceptions import ObjectDoesNotExist
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver



class Profile(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE,null=True,blank=True)
    user_name = models.CharField(max_length=60, blank=True)
    profile_photo = models.ImageField(default='default.jpg', upload_to='profile_pics')
    user_email = models.EmailField(max_length=255,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)


    @receiver(post_save, sender=Users)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(users=instance)
    @receiver(post_save, sender=Users) 
    def save_profile(sender,instance,**kwargs):
        instance.profile.save()  
