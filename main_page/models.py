from django.db import models

# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField


class Ticket(models.Model):
    name = models.CharField(max_length=50)
    phone = PhoneNumberField(null=False, region='UA', unique=False)
    time_create = models.DateTimeField(auto_now_add=True)
    is_message = models.BooleanField(default=False)

    def __str__(self):
        return '{} ({})'.format(self.name, self.phone)