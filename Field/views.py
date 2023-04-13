from django.shortcuts import render, redirect
from .models import Field, Spraying, Harvest, Fertilization, NPK_Product, NPK_Field
from .forms import FieldForm, SprayingForm, HarvestForm, FertilizationForm, NPK_FieldForm, NPK_ProductFrom
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



#### NPK ####
"""Main view in NPK with options to: add field NPK values, 
add new product, count amount of product to use on field"""
# MAIN
def fieldNPK(request, pk):
    field = Field.objects.get(id=pk)
    measurement = NPK_Field.objects.filter(field=pk)
    product = NPK_Product.objects.all()
    context = {
        "field" : field,
        "measurement" : measurement,
        "product" : product,
    }

    return render(request, "Field/npk_table.html", context)

##### FIELD NPK #####
# View to add new field NPK value, triggered by one of 3 buttons
def field_values_NPK(request, pk):
    field = get_object_or_404(Field, id=pk)
    
    if request.method == "POST":
        form = NPK_FieldForm(request.POST)
        if form.is_valid():
            new_npk = form.save(commit=False)
            new_npk.field = field
            new_npk.save()
        return redirect(f"/field/npk/{pk}")
    else:
        form = NPK_FieldForm()

    context = {
        "form" : form,
        "field" : field,
    }

    return render(request, "Field/npk_add_field_values.html", context)

# Delete Field NPK
def delete_field_values_NPK(request, pk):
    model_instance = NPK_Field.objects.get(id=pk)
    related_field = model_instance.field.pk
    NPK_Field.objects.filter(id = pk).delete()
    
    return redirect(f"/field/npk/{related_field}")


# Update Field NPK
def update_field_values_NPK(request, pk):
    model_instance = NPK_Field.objects.get(id=pk)
    field = get_object_or_404(Field, id=pk)
    
    if request.method == "POST":
        form = NPK_FieldForm(request.POST, instance=model_instance)
        if form.is_valid():
            new_npk = form.save(commit=False)
            new_npk.field = field
            new_npk.save()
        return redirect(f"/field/npk/{pk}")
    else:
        form = NPK_FieldForm(instance=model_instance)

    context = {
        "form" : form,
        "field" : field,
    }

    return render(request, "Field/npk_add_field_values.html", context)


##### PRODUCT #####
# list of products
def product_list_NPK(request):
    product = NPK_Product.objects.all()
    context = {
        "product" : product,
    }

    return render(request, "Field/product_list.html", context)


# create product
def add_product_NPK(request, pk):
    if request.method == "POST":
        form = NPK_ProductFrom(request.POST)
        if form.is_valid():
            form.save()
            
        return redirect(f"/field/npk/{pk}")
    else:
        form = NPK_ProductFrom()
    context = {
        "form" : form,
    }
    return render(request, "Field/npk_add_product.html", context)

# delete product
def delete_product_NPK(request, pk):
    NPK_Product.objects.filter(id = pk).delete()
    return redirect("/field/npk/product_list/")


#update product
def update_product_NPK(request, pk):
    product = NPK_Product.objects.get(id = pk)
    if request.method == "POST":
        form = NPK_ProductFrom(request.POST, instance = product)
        if form.is_valid():
            form.save()
            
        return redirect(f"/field/npk/{pk}")
    else:
        form = NPK_ProductFrom(instance = product)
    context = {
        "form" : form,
    }
    return render(request, "Field/npk_add_product.html", context)


#### Calculations ####
# View to count amount of product to use on vield, triggered by one of 3 buttons
def count_product_NPK(request, pk):
    context = {

    }
    return render(request, "Field/npk_table.html", context) 
