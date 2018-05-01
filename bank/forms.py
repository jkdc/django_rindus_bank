from django import forms

from bank.models import Person, Account


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        exclude = ['admin_person']

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['iban']