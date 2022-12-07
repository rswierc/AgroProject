from django.contrib import admin
from .models import Cow

# Register your models here.
@admin.register(Cow)
class CowAdmin(admin.ModelAdmin):
    list_display = ['earring_number', 'birth_date' , 'sex']