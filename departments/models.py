from django.db import models
from django.conf import settings
from authentication.models import User
from profiles.models import Profile



class Department(models.Model):
    """Department model class."""
    code = models.CharField(max_length=4, primary_key=True)
    name = models.CharField(max_length=30, blank=False, unique=True)
    dept_head = models.ForeignKey(settings.AUTH_USER_MODEL,blank=True, related_name='departments', on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name)

    def __unicode__(self):
        return self.name


class Employee(User, models.Model):
    """Employee model class."""
    first_name = models.CharField(max_length=255, blank=False, unique=True)
    last_name = models.CharField(max_length=255, blank=False, unique=True)
    phone_number = models.IntegerField(blank=True, unique=True, null=True)
    employee_number = models.IntegerField(blank=True, unique=True, null=True)
    gender = models.CharField(max_length=100, choices=(("Male", ("Male")),("Female", "Female")))
    designition = models.CharField(max_length=255, blank=True, unique=False)
    basic_pay = models.IntegerField(blank=True, default=0)
    department = models.ForeignKey(Department, related_name='employees', on_delete=models.CASCADE, blank=True, null=True)
    city = models.CharField(blank=True, max_length=100)
    county = models.CharField(blank=True, max_length=100)
    nationality = models.CharField(blank=True, max_length=100)
    country_of_residence = models.CharField(blank=True, max_length=100)
    postal_address = models.IntegerField(blank=True, null=True)
    

    

    def __str__(self):
        return '{}'.format(self.first_name)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('first_name',)

