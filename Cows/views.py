from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateNewCow, CowForm
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
    else:
        form = CreateNewCow() 
    
    return render(request, "Cows/create.html", {"form": form})


def createCow(request):
    if request.method == 'POST':
        form = CowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/cow/table")
    else:
        form = CowForm() 
    
    context = {"form": form}
    return render(request, "Cows/order_form.html", context)


def updateCow(request, pk):
    cow = Cow.objects.get(id = pk)
    form = CowForm(instance=cow)

    if request.method == 'POST':
        form = CowForm(request.POST, instance=cow)
        if form.is_valid():
            form.save()
            return redirect("/cow/table")
    
    context = {"form": form}
    return render(request, "Cows/order_form.html", context)


def deleteCow(request, pk):
    Cow.objects.filter(id=pk).delete()
    form = CowForm()
    return render(request, 'Cows/table.html', {"cows": Cow.objects.all()})


def sortEaringNum(request): #sortowanie
    sorted_cows = Cow.objects.all().order_by('birth_date').values()
    context = {
        'cows': sorted_cows,
    }

    return render(request, 'Cows/table.html', context)

def searchEaringNum(request):
    if request.method == "GET":
        earring_num = request.GET["earring_num"]
    
    cows = Cow.objects.filter(earring_number=earring_num).values()
    context = {"cows": cows}
    return render(request, "Cows/table.html", context)