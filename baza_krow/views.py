from django.shortcuts import render
from django.http import HttpResponse
from .forms import KrowaForm
from datetime import datetime
from .models import Post
from .forms import PostForm

# New view
def welcome(request):
    return render(request, "baza_krow/welcome.html",
    {"current_time": datetime.now(), #aktualny czas
    "posts": Post.objects.all(), #zwracam wszystkie elementy bazy danych
    "num_posts": Post.objects.count()}) #zwracam liczbe elementow


def new(request):
    if request.method == 
    form = PostForm(request.Post)
    return render(request, "baza_krow/welcome.html",
    {"form": form})