from django.forms import ModelForm
from .models import Krowa


class KrowaForm(ModelForm):
    class Meta:
        model = Krowa
        fields = '__all__'