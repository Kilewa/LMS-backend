from django.db import models
from django.conf import settings
import datetime

# Create your models here.

class leave(models.Model):
    choices = (
        ("Pending","Pending"),
        ("Approved", "Approved"),
        ("Denied", "Denied")
    )

    Employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    reasons = models.TextField(default="Annual Leave")
    status = models.CharField(max_length=10, choices= choices, default="Pending")
    comments = models.TextField(default='under review')

    def __str__(self):
        return '{}'.format(self.reasons)







