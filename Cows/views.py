from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateNewCow, ID
from .models import Cow



def cows_table(request):
    return render(request, "Cows/table.html", {
        "cows": Cow.objects.all(),
    })

def get_cow(request):
    if request.method == 'POST':
        form = CreateNewCow(request.POST)
        if form.is_valid():
            m = form.cleaned_data["earring_number"]
            n = form.cleaned_data["birth_date"]
            o = form.cleaned_data["sex"]
            t = Cow(earring_number=m, birth_date=n, sex=o)
            t.save()
            return HttpResponse("Thanks, all data is valid")
    else: #if it is smth else create blank class
        form = CreateNewCow() 
    
    return render(request, "Cows/create.html", {"form": form})


def delete(request, id):
    cow_to_delete = Cow.objects.filter(ID = id)
    cow_to_delete.delete()
    
