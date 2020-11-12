from django.db import models
from authentication.models import Users
import datetime

# Create your models here.

class leave(models.Model):

    Employee = models.ForeignKey(Users, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    reasons = models.TextField()
    comments = models.TextField()
    status = models.BooleanField(default=False)













