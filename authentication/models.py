from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)



class UserManager(BaseUserManager):

    def create_staff(self, username,email, password=None):
        user = self.model(
            username=username,
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.is_staff = True
        user.save(using=self.db)
        return user

    def create_dept_head(self, username,email,password=None):
        user = self.create_dept_head(username,email,password)
        user.is_dep_head = True
        user.is_staff = True
        user.save()
        return user

    def create_superuser(self, username,email,password=None):
        user = self.create_superuser(username=username ,email=self.normalize_email(email), password=password)
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user


class Users(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_dept_head = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # storing timestamps for users.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    added_by = models.ForeignKey("self", models.CASCADE, default=None, null=True)

    objects = UserManager()
    
    REQUIRED_FIELDS = ["username"]
    EMAIL_FIELD = "email"
    USERNAME_FIELD = 'email'


    
    

    def __str__(self):
        return self.email
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

