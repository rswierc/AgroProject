from django.shortcuts import render, redirect
from .models import Field, Spraying, Harvest, Fertilization
from .forms import FieldForm, SprayingForm, HarvestForm, FertilizationForm
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.db import IntegrityError

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
            try:
                form.save()
            except IntegrityError:
                context = {
                    "form": form,
                    "error_message": "ar_label must be unique"
                }
                return render(request, "Field/create.html", context)
            return redirect("/field/table.html")
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

# SORTING #
def sortField_area(request):
    sorted_fields = Field.objects.all().order_by('-area').values()

    context = {
        "field" : sorted_fields,
    }

    return render(request, "Field/table.html", context)


def sortField_location(request):
    sorted_fields = Field.objects.all().order_by('location').values()

    context = {
        "field" : sorted_fields,
    }

    return render(request, "Field/table.html", context)


def sortField_present(request):
    sorted_fields = Field.objects.all().order_by('present_seed').values()

    context = {
        "field" : sorted_fields,
    }

    return render(request, "Field/table.html", context)


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
        return redirect(f"/field/treatment/{pk}")
    else:
        form = SprayingForm()

    context = {
        "form" : form,
    }
    return render(request, "Field/create_spraying.html", context)

# Delete spraying
def deleteSpraying(request, pk):
    model_instance = Spraying.objects.get(id=pk)
    related_field = model_instance.field.pk

    Spraying.objects.filter(id = pk).delete()
    return redirect(f"/field/treatment/{related_field}")


# Update sparying 
def updateSpraying(request, pk):
    spraying = Spraying.objects.get(id=pk)
    related_field = spraying.field.pk
    form = SprayingForm(instance=spraying)

    if request.method == "POST":
        form = SprayingForm(request.POST, instance=spraying)
        if form.is_valid():
            form.save()
            return redirect(f"/field/treatment/{related_field}")
    
    context = {
        "form" : form,
    }
    return render(request, "Field/create_spraying.html", context)



#### HARVEST ####
# Create harvest
def harvestField(request, pk):
    field = get_object_or_404(Field, id=pk)
    
    if request.method == "POST":
        form = HarvestForm(request.POST)
        if form.is_valid():
            new_harvest = form.save(commit=False)
            new_harvest.field = field
            new_harvest.save()
        return redirect(f"/field/treatment/{pk}")
    else:
        form = HarvestForm()

    context = {
        "form" : form,
    }
    return render(request, "Field/create_harvest.html", context)


# Delete harvest
def deleteHarvest(request, pk):
    model_instance = Harvest.objects.get(id=pk)
    related_field = model_instance.field.pk
    Harvest.objects.filter(id = pk).delete()
    
    return redirect(f"/field/treatment/{related_field}")


# Update harvest 
def updateHarvest(request, pk):
    harvest = Harvest.objects.get(id=pk)
    related_field = harvest.field.pk
    form = HarvestForm(instance=harvest)

    if request.method == "POST":
        form = HarvestForm(request.POST, instance=harvest)
        if form.is_valid():
            form.save()
            return redirect(f"/field/treatment/{related_field}")
    
    context = {
        "form" : form,
    }
    return render(request, "Field/create_harvest.html", context)



#### FERTILIZATION ####
# Create fertilization 
def fertilizationField(request, pk):
    field = get_object_or_404(Field, id=pk)
    
    if request.method == "POST":
        form = FertilizationForm(request.POST)
        if form.is_valid():
            new_fertilization = form.save(commit=False)
            new_fertilization.field = field
            new_fertilization.save()
        return redirect(f"/field/treatment/{pk}")
    else:
        form = FertilizationForm()

    context = {
        "form" : form,
    }
    return render(request, "Field/create_fertilization.html", context)

# Delete fertilization
def deleteFertilization(request, pk):
    model_instance = Fertilization.objects.get(id=pk)
    related_field = model_instance.field.pk
    Fertilization.objects.filter(id = pk).delete()
    
    return redirect(f"/field/treatment/{related_field}")


# Update fertilization
def updateFertilization(request, pk):
    fertilization = Fertilization.objects.get(id=pk)
    related_field = fertilization.field.pk
    form = FertilizationForm(instance=fertilization)

    if request.method == "POST":
        form = FertilizationForm(request.POST, instance=fertilization)
        if form.is_valid():
            form.save()
            return redirect(f"/field/treatment/{related_field}")
    
    context = {
        "form" : form,
    }
    return render(request, "Field/create_fertilization.html", context)