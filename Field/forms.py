from .models import Field, Harvest, Spraying, Fertilization, NPK_Field, NPK_Product
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


class SprayingForm(forms.ModelForm):
    class Meta:
        model = Spraying
        exclude = ('field', )
        fields = ['field', 'type', 'amount']
        widgets = {
            'type': forms.TextInput(attrs={'class': 'form-control'}),
            'amount' : forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels ={
            'type' : "Środek",
            'amount' : "Ilość"
        }

class FertilizationForm(forms.ModelForm):
    class Meta:
        model = Fertilization
        exclude = ('field', )
        fields = ['type', 'amount']
        widgets = {
            'type': forms.TextInput(attrs={'class': 'form-control'}),
            'amount' : forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels ={
            'type' : "Środek",
            'amount' : "Ilość"
        }


class HarvestForm(forms.ModelForm):
    class Meta:
        model = Harvest
        exclude = ('field', )
        fields = ['harvest_date', 'hight']
        widgets = {
            'harvest_date': forms.DateInput(format=('%Y-%m-%d'),
                attrs={'class': 'form-control',
                        'type': 'date'}),
            'hight' : forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels ={
            'type' : "Środek",
            'amount' : "Ilość"
        }


class NPK_FieldForm(forms.ModelForm):
    class Meta:
        model = NPK_Field
        exclude = ('field',)
        fields = ['measurement_date', 'nitrogen_field', 'phosphorus_field', 'potassium_field']
        widgets = {
            'nitrogen_field' : forms.NumberInput(attrs={'class': 'form-control'}),
            'phosphorus_field' : forms.NumberInput(attrs={'class': 'form-control'}),
            'potassium_field' : forms.NumberInput(attrs={'class': 'form-control'}),
            'measurement_date' : forms.DateInput(format=('%Y-%m-%d'),
                attrs={'class': 'form-control',
                        'type': 'date'}),
        }

        labels = {
            'nitrogen_field' : "Azot[N]",
            'phosphorus_field' : "Fosfor[P]",
            'potassium_field' : "Potas[K]",
            'measurement_date' : "Data pomiaru",
        }


class NPK_ProductFrom(forms.ModelForm):
    class Meta:
        model = NPK_Product
        fields = '__all__'
        widgets = {
            'catalog_number' : forms.TextInput(attrs={'class': 'form-control'}),
            'product_firm' : forms.TextInput(attrs={'class': 'form-control'}),
            'product_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'nitrogen_product' : forms.NumberInput(attrs={'class': 'form-control'}),
            'phosphorus_product' : forms.NumberInput(attrs={'class': 'form-control'}),
            'potassium_product' : forms.NumberInput(attrs={'class': 'form-control'}),
            }
        
        labels = {
            'catalog_number' : 'Numer katalogowy',
            'product_firm' : 'Firma',
            'product_name' : 'Nazwa produktu',
            'nitrogen_product' : "Azot[N]",
            'phosphorus_product' : "Fosfor[P]",
            'potassium_product' : "Potas[K]",
        }
