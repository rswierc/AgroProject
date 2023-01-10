from django.contrib import admin
from .models import Field, Spraying

# Register your models here.
@admin.register(Field)
class Sheep(admin.ModelAdmin):
    list_display = ['field_number', 'area', 'location']


@admin.register(Spraying)
class Spraying(admin.ModelAdmin):
    list_display = ['field', 'type', 'amount']