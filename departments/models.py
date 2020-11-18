from django.db import models
from django.conf import settings
from authentication.models import User
from profiles.models import Profile



class Department(models.Model):
    """Department model class."""
    code = models.CharField(max_length=4, primary_key=True)
    name = models.CharField(max_length=30, blank=False, unique=True)

    def __str__(self):
        return '{}'.format(self.name)

    def __unicode__(self):
        return self.name


class Employee(User, models.Model):
    """Employee model class."""
    first_name = models.CharField(max_length=255, blank=False, unique=True)
    last_name = models.CharField(max_length=255, blank=False, unique=True)
    phone_number = models.IntegerField(blank=False, unique=True)
    employee_number = models.IntegerField(blank=False, unique=True)
    gender = models.CharField(max_length=100, choices=(("Male", ("Male")),("Female", "Female")))
    designition = models.CharField(max_length=255, blank=False, unique=False)
    basic_pay = models.IntegerField(blank=False, default=0)
    department = models.ForeignKey(Department, related_name='employees', on_delete=models.CASCADE)
    city = models.CharField(blank=False, max_length=100)
    dept_head = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='departments', on_delete=models.CASCADE)
    county = models.CharField(blank=False, max_length=100)
    nationality = models.CharField(blank=False, max_length=100)
    country_of_residence = models.CharField(blank=False, max_length=100)
    postal_address = models.IntegerField(blank=False)
    

    

    def __str__(self):
        return '{}'.format(self.first_name)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('first_name',)

