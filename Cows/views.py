from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CowForm, CowNote
from .models import Cow
from django.db.models.functions import Coalesce

# main table view
def tableCow(request):
    cows = Cow.objects.all()
    context = {
        'cows': cows,
    }
    return render(request, 'Cows/table.html', context)

# creating cow
def createCow(request):
    if request.method == 'POST':
        form = CowForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/cow/table")
    else:
        form = CowForm() 
    
    context = {"form": form}
    return render(request, "Cows/create.html", context)

# note cow
def noteCow(request, pk):
    cow = Cow.objects.get(id = pk)
    form = CowNote(instance=cow)

    if request.method == 'POST':
        form = CowNote(request.POST, instance=cow)
        if form.is_valid():
            form.save()
            return redirect("/cow/table")
    
    context = {"form": form}
    return render(request, "Cows/create.html", context)

# update cow
def updateCow(request, pk):
    cow = Cow.objects.get(id = pk)
    form = CowForm(instance=cow)

    if request.method == 'POST':
        form = CowForm(request.POST, instance=cow)
        if form.is_valid():
            form.save()
            return redirect("/cow/table")
    
    context = {"form": form}
    return render(request, "Cows/create.html", context)


# delete cow
def deleteCow(request, pk):
    Cow.objects.filter(id=pk).delete()
    return render(request, 'Cows/table.html', {"cows": Cow.objects.all()})


    

# search cow by earring number
def searchEaringNum(request):
    if request.method == "GET":
        earring_num = request.GET["earring_num"]
        cows = Cow.objects.filter(earring_number=earring_num).values()
        cows.update()
    else:
        cows = Cow.objects.all()
    
    context = {
        "cows": cows,
    }
    return render(request, "Cows/table.html", context)


# sort cows by date of birth, the oldest is the first one
def sortCow_birth(request):
    cows = Cow.objects.all().order_by("birth_date").values()
    context = {
        "cows": cows,
    }
    return render(request, "Cows/table.html", context)


# sort cows by sale price, the cheapest go first
def sortCow_sale(request):
    cows = Cow.objects.all().order_by("sale_price").values()
    context = {
        "cows": cows,
    }
    return render(request, "Cows/table.html", context)


# sort cow by sex, 'byk' go first
def sortCow_sex(request):
    cows = Cow.objects.all().order_by("sex").values()
    context = {
        "cows": cows,
    }
    return render(request, "Cows/table.html", context)

