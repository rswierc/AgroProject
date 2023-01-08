from django.shortcuts import render, redirect
from .models import Field, Spraying, Harvest, Fertilization
from .forms import FieldForm


# Fields table
def tableField(request):
    field = Field.objects.all()
    context = {
        'field': field,
    }
    return render(request, 'Field/table.html', context)


#Fields create
def createField(request):
    if request.method == "POST":
        form = FieldForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect("/field/table")
    else:
        form = FieldForm()

    context = {
        "form" : form,
    }
    return render(request, "Field/create.html", context)

# Field update
def updateField(request, pk):
    field = Field.objects.get(id = pk)
    form = FieldForm(instance=field)

    if request.method == "POST":
        form = FieldForm(request.POST, request.FILES, instance=field)
        if form.is_valid():
            form.save()
            return redirect("/field/table")

    context = {
        "form" : form,
        "field" : field,
    }

    return render(request, "Field/create.html", context)

#Field delete
def deleteField(request, pk):
    Field.objects.filter(id=pk).delete()
    field = Field.objects.all()

    context = {
        "field" : field,
    }
    return render(request, "Field/table.html", context)


#Field treatments 
def treatmentField(request, pk):
    spraying = Spraying.objects.get(id=pk)
    harvest = Harvest.objects.get(id=pk)
    fertilization = Fertilization.objects.get(id=pk)

    context = {
        "spraying" : spraying,
        "harvest" : harvest,
        "fertilization" : fertilization,
    }

    return render(request, "Field/treatment_main.html", context)

    
def sprayingField(request, pk):
    pass

def harvestField(request, pk):
    pass

def fertilizationField(request, pk):
    pass