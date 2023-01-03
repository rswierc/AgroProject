from .models import Cow
from django import forms

class CowForm(forms.ModelForm):
    class Meta:
        model = Cow
        fields = '__all__'
        widgets = {
            'birth_date': forms.DateInput()
        }

class CowNote(forms.ModelForm):
    class Meta:
        model = Cow
        fields = ('note',)