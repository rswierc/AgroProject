from .models import Cow
from django import forms



class CreateNewCow(forms.Form):
    earring_number = forms.CharField(label="Numer kolczyka", max_length=10)
    birth_date = forms.DateField(label="Data")
    sex = forms.CharField(max_length=5)

class CowForm(forms.ModelForm):
    class Meta:
        model = Cow
        fields = '__all__'
        widgets = {
            'birth_date': forms.DateInput()
        }