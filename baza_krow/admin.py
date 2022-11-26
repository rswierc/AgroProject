from django.contrib import admin
from.models import Krowa
from .models import Post

# Register your models here.
@admin.register(Krowa)
class KrowaAdmin(admin.ModelAdmin):
    list_display = ['earring_number', 'birth_date' , 'sex']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'body']