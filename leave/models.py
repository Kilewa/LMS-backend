from django.db import models
from authentication.models import Users
import datetime

# Create your models here.

class leave(models.Model):
    choices = (
        ("1", "Pending"),
        ("2", "Approved"),
        ("3", "Denied")
    )

    Employee = models.ForeignKey(Users, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    reasons = models.TextField()
    status = models.CharField(max_length=1, choices= choices)













