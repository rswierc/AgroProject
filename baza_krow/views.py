from django.shortcuts import render
from django.http import HttpResponse
from .forms import KrowaForm


# New view
def welcome(request):
    return render(request, "baza_krow/welcome.html")


