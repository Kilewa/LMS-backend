from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    BaseUserManager,AbstractBaseUser,PermissionsMixin
)
from rest_framework_simplejwt.tokens import RefreshToken

<<<<<<< HEAD


class Role(models.Model):
    '''
    The Role entries are managed by the system,
    automatically created via a Django data migration.
    '''
    EMPLOYEE = 1
    DEPT_HEAD = 2
    ADMIN = 3
    ROLE_CHOICES = (
        (EMPLOYEE, 'Employee'),
        (DEPT_HEAD, 'Dept_head'),
        (ADMIN, 'Admin')
    )

    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)
=======
class UserManager(BaseUserManager):
>>>>>>> 7676554a595c53ae9745e2b9c5c4c20ad005d266

    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('Users should have a username')
        if email is None:
            raise TypeError('Users should have a Email')

        user = self.model(
            username=username, 
            email=self.normalize_email(email),
            )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_employee(self, email,username,password=None):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email==self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_staff = True
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(
            email=self.normalize_email(email),
			password=password,
			username=username,)
            
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_dept_head = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email
    
    def tokens(self):
        refresh=RefreshToken.for_user(self)
        return{
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        }

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'