from django.db import models
from django.conf import settings
import datetime
from cloudinary.models import CloudinaryField
from users.models import Departmenthead

# Create your models here.

class Attendance(models.Model):

    attendance_choices = (
    ('absent', 'Absent'),
    ('present', 'Present')
)


    department_head = models.ForeignKey('Departmenthead', on_delete=models.SET_NULL, blank=True, null=True)
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    attendance = models.CharField(max_length=8, choices=attendance_choices, blank=True)

    class Meta():
        """
        docstring
        """
        pass

