from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    AbstractUser
)



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

    def __str__(self):
        return self.get_role_display()


class User(AbstractUser):
    roles = models.ManyToManyField(Role)