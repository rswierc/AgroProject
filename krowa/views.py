from django.shortcuts import render
from django.http import HttpResponse
from .models import Krowa



# Create your views here.
def KrowaView(request):
    return render(request, "krowa/base.html",
    {"korwy": Krowa.objects.all(), #dictionary
    "number": Krowa.objects.count()}
    )


def home(request):
    return render(request, "krowa/home.html",{
        "krowa": Krowa.objects.all(),
        "number": Krowa.objects.count(),
    }
    )
