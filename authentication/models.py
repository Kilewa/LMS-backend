from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    AbstractUser
)

class User(AbstractUser):
    USER_ROLES = (
        (1, 'DEPARTMENT HEAD'),
        (2, 'EMPLOYEE')
    )
    role = models.CharField(
        verbose_name='user role',max_length=2, choices=USER_ROLES
    )