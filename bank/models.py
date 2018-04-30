from django.contrib.auth.models import AbstractUser, User
from django.db import models
from localflavor.generic.models import IBANField

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    admin_person = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __unicode__(self):
        return self.first_name

class Account(models.Model):
    iban = IBANField()
    person = models.ForeignKey(Person, on_delete=models.CASCADE,)

    def __unicode__(self):
        return self.iban