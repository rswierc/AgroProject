from .models import Krowa
from django import forms

class CreateNewKrowa(forms.Form):
    earring_number = forms.CharField(label="Numer kolczyka", max_length=10)
    birth_date = forms.DateField()
    sex = forms.CharField(max_length=5)
