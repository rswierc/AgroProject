from django.shortcuts import render
from django.http import HttpResponse
from .models import Krowa
from .forms import CreateNewKrowa



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

def create(request):
    if request.method == 'POST': #check if it is post 
        form = CreateNewKrowa(request.POST)
        if form.is_valid(): # if the data is valid use it to pass values
            m = form.cleaned_data["earring_number"]
            n = form.cleaned_data["birth_date"]
            o = form.cleaned_data["sex"]
            t = Krowa(earring_number=m, birth_date=n, sex=o)
            t.save()
    else: #if it is smth else create blank class
        form = CreateNewKrowa()       

    return render(request, "krowa/create.html", {"form": form})
