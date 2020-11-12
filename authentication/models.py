from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)

class UserManager(BaseUserManager):

    def create_user(self, username,email, password=None):
        '''
        Creates a new staff profile object.
        '''
        if not email:
                raise ValueError('Users must have an email address')
        if not username:
                raise ValueError('Users must have a username')

        user = self.model(
            username=username,
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self.db)
        
        return user
    
    def create_staff(self, username,email,password=None):
        '''
        Creates a new department head profile object.
        '''

        user = self.create_user(username=username,email=self.normalize_email(email),password=password)
        user.is_staff = True
        user.save(using=self._db)

        return user

    def create_dept_head(self, username,email,password=None):
        '''
        Creates a new department head profile object.
        '''

        user = self.create_user(username=username,email=self.normalize_email(email),password=password)
        user.is_dept_head = True
        user.is_staff = True
        user.save(using=self._db)

        return user

    def create_superuser(self, username,email,password):
        '''
        Creates a new superuser.
        '''
        user = self.create_user(username=username ,email=self.normalize_email(email), password=password)
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True

        user.save(using=self._db)

        return user

class Users(AbstractBaseUser, PermissionsMixin):

    '''Represents a "user profile" inside our system.'''

    email = models.EmailField(max_length=160,verbose_name="email",unique=True)
    username = models.CharField(max_length=255)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_dept_head = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # storing timestamps for users.
    date_joined = models.DateTimeField(verbose_name='date joined',auto_now_add=True)
    last_login= models.DateTimeField(verbose_name='last login',auto_now=True)
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