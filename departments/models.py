from django.db import models
from django.conf import settings


class Department(models.Model)
    """Department model class."""
    code = models.CharField(max_length=4, primary_key=True)
    name = models.CharField(max_length=30, blank=False, unique=True)
    depart_head = models.ForeignKey(Users, related_name='departments', on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name)

    def __unicode__(self):
        return self.name


class Employee(models.Model):
    """Employee model class."""
    first_name = models.CharField(max_length=255, blank=False, unique=True)
    last_name = models.CharField(max_length=255, blank=False, unique=True)
    email = models.EmailField(blank=False, unique=True)
    phone_number = models.IntegerField(blank=False, unique=True)
    employee_number = models.IntegerField(blank=False, unique=True)
    gender = models.CharField(max_length=100, choices=(("Male", ("Male")),("Female", "Female")))
    designition = models.CharField(max_length=255, blank=False, unique=False)
    is_active = models.BooleanField(default=True)
    basic_pay = models.IntegerField(blank=False, default=0)
    department = models.ForeignKey(Department, related_name='employees', on_delete=models.CASCADE)
    depart_head = models.ForeignKey(Users, related_name='department', on_delete=models.CASCADE)
    city = models.CharField(blank=False, max_length=100)
    county = models.CharField(blank=False, max_length=100)
    nationality = models.CharField(blank=False, max_length=100)
    country_of_residence = models.CharField(blank=False, max_length=100)
    postal_address = models.IntegerField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return '{}'.format(self.first_name)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('first_name',)

