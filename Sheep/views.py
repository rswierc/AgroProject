from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SheepForm, SheepNote
from .models import Sheep
from django.db.models.functions import Coalesce

# main table view
def tableSheep(request):
    sheep = Sheep.objects.all()
    context = {
        'sheep': sheep,
    }
    return render(request, 'Sheep/table.html', context)

# creating cow
def createSheep(request):
    if request.method == 'POST':
        form = SheepForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/sheep/table")
    else:
        form = SheepForm() 
    
    context = {"form": form}
    return render(request, "Sheep/create.html", context)

# note cow
def noteSheep(request, pk):
    sheep = Sheep.objects.get(id = pk)
    form = SheepNote(instance=sheep)

    if request.method == 'POST':
        form = SheepNote(request.POST, instance=sheep)
        if form.is_valid():
            form.save()
            return redirect("/sheep/table")
    
    context = {"form": form}
    return render(request, "Sheep/create.html", context)

# update cow
def updateSheep(request, pk):
    sheep = Sheep.objects.get(id = pk)
    form = SheepForm(instance=sheep)

    if request.method == 'POST':
        form = SheepForm(request.POST, instance=sheep)
        if form.is_valid():
            form.save()
            return redirect("/sheep/table")
    
    context = {"form": form}
    return render(request, "Sheep/create.html", context)


# delete cow
def deleteSheep(request, pk):
    Sheep.objects.filter(id=pk).delete()
    sheep = Sheep.objects.all()
    context = {
        'sheep' : sheep
    }
    return render(request, 'Sheep/table.html', context)


    
# search cow by earring number
def searchEaringNum(request):
    if request.method == "GET":
        earring_num = request.GET["earring_num"]
        sheep = Sheep.objects.filter(earring_number=earring_num).values()
        sheep.update()
    else:
        sheep = Sheep.objects.all()
    
    context = {
        "sheep": sheep,
    }
    return render(request, "Sheep/table.html", context)


# sort cows by date of birth, the oldest is the first one
def sortSheep_birth(request):
    sheep = Sheep.objects.all().order_by("birth_date").values()
    context = {
        "sheep": sheep,
    }
    return render(request, "Sheep/table.html", context)


# sort cows by sale price, the cheapest go first
def sortSheep_sale(request):
    sheep = Sheep.objects.all().order_by("sale_price").values()
    context = {
        "sheep": sheep,
    }
    return render(request, "Sheep/table.html", context)


# sort cow by sex, 'byk' go first
def sortSheep_sex(request):
    sheep = Sheep.objects.all().order_by("sex").values()
    context = {
        "sheep": sheep,
    }
    return render(request, "Sheep/table.html", context)


