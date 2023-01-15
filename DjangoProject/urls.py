from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from Cows import views as CowView
from MainPage import views as MainPageView
from Sheep import views as SheepView
from Field import views as FieldView

urlpatterns = [
    path('admin/', admin.site.urls),
    #main page urls
    path('', MainPageView.weather),
    #cow urls
    path('cow/table/', CowView.tableCow),
    path('cow/create/', CowView.createCow, name="create_cow"),
    path('cow/update/<str:pk>', CowView.updateCow, name="update_cow"),
    path('cow/delete/<str:pk>', CowView.deleteCow, name="delete_cow"),
    path('cow/note/<str:pk>', CowView.noteCow, name="note_cow"),
    path('cow/search', CowView.searchEaringNum, name="cow/search"),
    path('cow/sort/birth', CowView.sortCow_birth, name="sort_birth_date"),
    path('cow/sort/sale', CowView.sortCow_sale, name="sort_birth_sale"),
    path('cow/sort/sex', CowView.sortCow_sex, name="sort_birth_sex"),

    #sheep urls
    path('sheep/table/', SheepView.tableSheep),
    path('sheep/create/', SheepView.createSheep, name="create_sheep"),
    path('sheep/update/<str:pk>', SheepView.updateSheep, name="update_sheep"),
    path('sheep/delete/<str:pk>', SheepView.deleteSheep, name="delete_sheep"),
    path('sheep/note/<str:pk>', SheepView.noteSheep, name="note_sheep"),
    path('sheep/search', SheepView.searchEaringNum, name="sheep/search"),
    path('sheep/sort/birth', SheepView.sortSheep_birth, name="sort_birth_date"),
    path('sheep/sort/sale', SheepView.sortSheep_sale, name="sort_birth_sale"),
    path('sheep/sort/sex', SheepView.sortSheep_sex, name="sort_birth_sex"),

    # field urls
    path('field/table/', FieldView.tableField),
    path('field/create/', FieldView.createField, name="create_field"),
    path('field/update/<str:pk>', FieldView.updateField, name="update_field"),
    path('field/delete/<str:pk>', FieldView.deleteField, name="delete_field"),
    path('field/treatment/<str:pk>', FieldView.treatmentField, name="treatment_field"),
    path('field/sort/location', FieldView.sortField_location, name="sort_location"),
    path('field/sort/area', FieldView.sortField_area, name="sort_area"),
    path('field/sort/present', FieldView.sortField_present, name="sort_present"),
    path('field/npk/<str:pk>', FieldView.fieldNPK, name="fieldNPK"), #main NPK view (npk.table.html)

    # field spraying 
    path('field/treatment/spraying_create/<str:pk>', FieldView.sprayingField, name="spraying_create"),
    path('field/treatment/spraying_delete/<str:pk>', FieldView.deleteSpraying, name="spraying_delete"),
    path('field/treatment/spraying_update/<str:pk>', FieldView.updateSpraying, name="spraying_update"),
    # field fertilization 
    path('field/treatment/fertilization_create/<str:pk>', FieldView.fertilizationField, name="fertilization_create"),
    path('field/treatment/fertilization_delete/<str:pk>', FieldView.deleteFertilization, name="fertilization_delete"),
    path('field/treatment/fertilization_update/<str:pk>', FieldView.updateFertilization, name="fertilization_update"),
    # field harvest
    path('field/treatment/harvest_create/<str:pk>', FieldView.harvestField, name="harvest_create"),
    path('field/treatment/harvest_delete/<str:pk>', FieldView.deleteHarvest, name="harvest_delete"),
    path('field/treatment/harvest_update/<str:pk>', FieldView.updateHarvest, name="harvest_update"),

    #### NPK FILED ####
    # new field npk values
    path('field/npk/add_field_values/<str:pk>', FieldView.field_values_NPK, name="field_values"), #add field npk values (npk_add_field_values)
    path('field/npk/delete/<str:pk>', FieldView.delete_field_values_NPK, name="field_npk_delete"),
    path('field/treatment/fertilization_update/<str:pk>', FieldView.updateFertilization, name="fertilization_update"),
    # new products
    path('field/npk/add_product/<str:pk>', FieldView.add_product_NPK, name="add_product"), #add new product
    # count
    path('field/npk/count_product_npk/<str:pk>', FieldView.count_product_NPK, name="count_product"), #count amount of product to use



    

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
