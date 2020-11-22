from django.db import models
from django.conf import settings
import datetime
from cloudinary.models import CloudinaryField

# Create your models here.

class expenses(models.Model):
    choices = (
        ("Pending","Pending"),
        ("Approved", "Approved"),
        ("Denied", "Denied")
    )

    Employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    location = models.TextField()
    price = models.CharField(max_length=64, blank=True)
    purchase_date = models.DateTimeField()
    bill = CloudinaryField('image')
    status = models.CharField(max_length=10, choices= choices, default="Pending")

    def __str__(self):
        return '{}'.format(self.location)

    class Meta:
        verbose_name = 'expense'


