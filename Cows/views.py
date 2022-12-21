from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CowForm, SortingForm
from .models import Cow

def cows_table(request):
    cows = Cow.objects.all()
    context = {
        'cows': cows,
    }
    return render(request, 'Cows/table.html', context)


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
    return render(request, 'Cows/table.html', {"cows": Cow.objects.all()})
    
    
def sortCow(request):
    if request.method == "POST":
        form = SortingForm(request.POST)
        if form.is_valid():
            m = form.cleaned_data["choice"]
            sorted_cows = Cow.objects.all().order_by(m).values()
    else:
        sorted_cows = Cow.objects.all()
    
    form = SortingForm()
    context = {
        'form': form,
        'cows': sorted_cows,
    }
    return render(request, 'Cows/table.html', context)


def searchEaringNum(request):
    if request.method == "GET":
        earring_num = request.GET["earring_num"]
        cows = Cow.objects.filter(earring_number=earring_num).values()
    else:
        cows = Cow.objects.all()
    
    context = {
        "cows": cows,
    }
    return render(request, "Cows/table.html", context)