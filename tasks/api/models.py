from django.db import models
from django.conf import settings

# Create your models here.

class task(models.Model):
    choices = (
        ("Complete","Complete"),
        ("Incomplete", "Incomplete"),
    )
    name = models.CharField(max_length=100)
    assigned_on = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices= choices, default="Incomplete")


    def __str__(self):
        return '{}'.format(self.name)

