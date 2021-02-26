from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class PhonebookItem(models.Model):
    name = models.CharField(max_length=255)
    phone_number = PhoneNumberField()

    class Meta:
        ordering = ['id',]