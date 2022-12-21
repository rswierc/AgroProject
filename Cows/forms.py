from .models import Cow, Sorting
from django import forms

class CowForm(forms.ModelForm):
    class Meta:
        model = Cow
        fields = '__all__'
        widgets = {
            'birth_date': forms.DateInput()
        }

class SortingForm(forms.ModelForm):
    class Meta:
        model = Sorting
        fields = '__all__'