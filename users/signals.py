from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser,Departmenthead, Employee
from .send_email import send_confirmation_email
@receiver(post_save, sender=CustomUser)
def create_profile_signal(sender, instance, created, **kwargs):
    if created:
        if instance.role==2:
            Departmenthead.objects.create(user=instance)
            instance.departmenthead.save()
            send_confirmation_email(instance)
        elif instance.role==3:
            Employee.objects.create(user=instance)
            instance.employee.save()
            send_confirmation_email(instance)  