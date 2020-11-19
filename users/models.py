from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

from .managers import CustomUserManager

# Create your models here.

class CustomUser(AbstractUser):

    # These fields tie to the roles!
    ADMIN = 1
    DEPARTMENTHEAD= 2
    Employee = 3

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (DEPARTMENTHEAD, 'Departmenthead'),
        (Employee, 'Employee')
    )

    username = None
    email = models.EmailField(('email address'), unique=True)
    is_active=models.BooleanField(default=True)
    is_verified=models.BooleanField(default=False)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES)
    address = models.CharField(max_length=200,blank=True,null=True)
    mobile = models.CharField(max_length=20,blank=True,null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email



departments=[('Administration','Adminstration'),
('Accounting and Finance', 'Accounting and Finance'),
('Sales and Marketing','Sales and Marketing'),
('Credit Control','Credit Control'),
('Accounting and Finance','Accounting and Finance'),
('Customer Relations','Customer Relations'),
('Quality Control','Quality Control'), ('Purchasing', 'Purchasing')
]

class Departmenthead(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    department= models.CharField(max_length=50,choices=departments,default='Adminstration')
    
    
    def __str__(self):
        return "{} ({})".format(self.user.first_name,self.department)


class Employee(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, blank=False, unique=True)
    last_name = models.CharField(max_length=255, blank=False, unique=True)
    phone_number = models.IntegerField(blank=True, unique=True, null=True)
    employee_number = models.IntegerField(blank=True, unique=True, null=True)
    gender = models.CharField(max_length=100, choices=(("Male", ("Male")),("Female", "Female")))
    designition = models.CharField(max_length=255, blank=True, unique=False)
    basic_pay = models.IntegerField(blank=True, default=0)
    department= models.CharField(max_length=50,choices=departments,default='Administration')
    city = models.CharField(blank=True, max_length=100)
    county = models.CharField(blank=True, max_length=100)
    nationality = models.CharField(blank=True, max_length=100)
    country_of_residence = models.CharField(blank=True, max_length=100)
    postal_address = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return "{} ({}:{})".format(self.user.first_name,self.user.get_role_display(),self.gender)

