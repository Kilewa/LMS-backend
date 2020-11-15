from django.db import models
from authentication.models import Users
import datetime

# Create your models here.

class leave(models.Model):
    choices = (
        ("Pending","Pending"),
        ("Approved", "Approved"),
        ("Denied", "Denied")
    )

    Employee = models.ForeignKey(Users, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    reasons = models.TextField()
    status = models.CharField(max_length=10, choices= choices, default="Pending")
    comments = models.TextField(default='under review')












