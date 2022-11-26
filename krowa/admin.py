from django.contrib import admin
from .models import Krowa

# Register your models here.
@admin.register(Krowa)
class KrowaAdmin(admin.ModelAdmin):
    list_display = ['earring_number', 'birth_date' , 'sex']