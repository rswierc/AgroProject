from django.contrib import admin
from .models import Sheep

# Register your models here.
@admin.register(Sheep)
class Sheep(admin.ModelAdmin):
    list_display = ['earring_number', 'birth_date' , 'sex']
