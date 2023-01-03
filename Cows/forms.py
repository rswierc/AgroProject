from .models import Cow
from django import forms

class CowForm(forms.ModelForm):
    class Meta:
        model = Cow
        fields = '__all__'
        widgets = {
            'earring_number' : forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(format=('%Y-%m-%d'),
                 attrs={'class': 'form-control', 
                    'type': 'date'}),
            'sex' : forms.Select(attrs={'class': 'form-control'}),
            'buyer' : forms.TextInput(attrs={'class': 'form-control'}),
            'sale_price' : forms.NumberInput(attrs={'class': 'form-control'}),
            'sale_date' : forms.DateInput(format=('%Y-%m-%d'),
                 attrs={'class': 'form-control', 
                'type': 'date'}),
            'calving_date' : forms.DateInput(format=('%Y-%m-%d'),
                 attrs={'class': 'form-control', 
                'type': 'date'}),
            'estrus_date' : forms.DateInput(format=('%Y-%m-%d'),
                 attrs={'class': 'form-control', 
                'type': 'date'}),
            'note' : forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'earring_number' : "Numer kolczyka",
            'birth_date': "Data urodzenia",
            'sex' : "Płeć",
            'buyer' : "Kupiec",
            'sale_price' : "Cena sprzedaży",
            'sale_date' : "Data sprzedaży",
            'calving_date' : "Data wycielenia",
            'estrus_date' : "Data rui",
            'note' : "Notatki",
        }

class CowNote(forms.ModelForm):
    class Meta:
        model = Cow
        fields = ('note',)