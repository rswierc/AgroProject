from django.shortcuts import render, redirect
from .models import Field, Spraying, Harvest, Fertilization
from .forms import FieldForm, SprayingForm, HarvestForm, FertilizationForm
from django.shortcuts import get_object_or_404

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


#Show field treatments 
def treatmentField(request, pk):
    field = Field.objects.get(id=pk)
    spraying = Spraying.objects.filter(field=pk)
    harvest = Harvest.objects.filter(field=pk)
    fertilization = Fertilization.objects.filter(field=pk)

    context = {
        "field" : field,
        "spraying" : spraying,
        "harvest" : harvest,
        "fertilization" : fertilization,
    }

    return render(request, "Field/treatment_main.html", context)

###### SPRAYING ######
# Create spraying
def sprayingField(request, pk):
    field = get_object_or_404(Field, id=pk)
    
    if request.method == "POST":
        form = SprayingForm(request.POST)
        if form.is_valid():
            new_spraying = form.save(commit=False)
            new_spraying.field = field
            new_spraying.save()
        return redirect("/field/table")
    else:
        form = SprayingForm()

    context = {
        "form" : form,
    }
    return render(request, "Field/create_spraying.html", context)

# Delete spraying
def deleteSpraying(request, pk):
    Spraying.objects.filter(field = pk).delete()
    spraying = Spraying.objects.filter(field = pk)

    context = {
        "spraying" : spraying,
    }

    return render(request, "Field/treatment_main.html", context)




# Create harvest
def harvestField(request, pk):
    if request.method == "POST":
        form = HarvestForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/field/table")
    else:
        form = HarvestForm()

    context = {
        "form" : form,
    }
    return render(request, "Field/harvest.html", context)


# Create fertilization 
def fertilizationField(request, pk):
    if request.method == "POST":
        form = FertilizationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/field/table")
    else:
        form = FertilizationForm()

    context = {
        "form" : form
    }

    return render(request, "Field/fertilization.html", context)