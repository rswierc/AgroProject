from .models import Field
from django import forms

class FieldForm(forms.ModelForm):
    class Meta:
        model = Field
        fields = '__all__'
        widgets = {
            'field_number' : forms.TextInput(attrs={'class': 'form-control'}),
            'ar_label': forms.TextInput(attrs={'class': 'form-control'}),
            'area' : forms.NumberInput(attrs={'class': 'form-control'}),
            'location' : forms.Select(attrs={'class': 'form-control'}),
            #'field_image' : forms.ImageField(),
            'soil_richness' : forms.NumberInput(attrs={'class': 'form-control'}),
            'acidity' : forms.NumberInput(attrs={'class': 'form-control'}),
            'last_seed' : forms.TextInput(attrs={'class': 'form-control'}),
            'present_seed' : forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'field_number' : "Numer działki",
            'ar_label': "Nr Agencji Restrukturyzacji i Modernizacji Rolnictwa",
            'area' : "Powierzchnia",
            'location' : "Lokalizacja",
            'field_image' : "Zdjęcie",
            'soil_richness' : "Zasobność gleby",
            'acidity' : "Kawsowość",
            'last_seed' : "Poprzednia uprawa ",
            'present_seed' : "Obecna uprawa",
        }

class FieldNote(forms.ModelForm):
    class Meta:
        model = Field
        fields = '__all__'
        widgets = {

        }
        labels ={
        
        }