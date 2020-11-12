from django.db import models
from authentication.models import Users

# Create your models here.

class task(models.Model):
    name = models.CharField(max_length=100)
    assigned_on = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    assigned_to = models.ForeignKey(Users, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
