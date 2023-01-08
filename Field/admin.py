from django.contrib import admin
from .models import Field

# Register your models here.
@admin.register(Field)
class Sheep(admin.ModelAdmin):
    list_display = ['field_number', 'area', 'location']