from django.contrib import admin

# Register your models here.
from bank.models import Account, Person

admin.site.register(Person)
admin.site.register(Account)
